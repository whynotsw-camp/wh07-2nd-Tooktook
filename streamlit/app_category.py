import streamlit as st
import pandas as pd 
import matplotlib as mpl
import plotly.express as px

def category_char1(customers_df, consultations_df):
    """
    FastAPI에서 받아온 데이터를 사용하는 카테고리별 분석 함수
    """
    # 한글폰트
    mpl.rcParams['font.family'] = 'Noto Sans KR'
    mpl.rcParams['axes.unicode_minus'] = False
    
    # 공통 CSS
    tooltip_css = """
    <style>
    .tooltip {
      position: relative;
      display: inline-block;
      cursor: pointer;
      font-size: 16px;
      margin-left: 2px;
    }
    .tooltip .tooltiptext {
      visibility: hidden;
      min-width: 300px;
      max-width: 600px;
      background-color: #333;
      color: #fff;
      text-align: left;
      border-radius: 6px;
      padding: 10px;
      position: absolute;
      z-index: 1;
      bottom: 125%;
      left: 50%;
      transform: translateX(-50%);
      opacity: 0;
      transition: opacity 0.3s;
      font-size: 14px;
      line-height: 1.4;
    }
    .tooltip:hover .tooltiptext {
      visibility: visible;
      opacity: 1;
    }
    </style>
    """
    st.markdown(tooltip_css, unsafe_allow_html=True)

    # 데이터 복사 및 병합
    customers_df = customers_df.copy()
    consultations_df = consultations_df.copy()
    consultations_df['start_time'] = pd.to_datetime(consultations_df['start_time'])
    consultations_df['end_time'] = pd.to_datetime(consultations_df['end_time'])
    consultations_df['consultation_date'] = pd.to_datetime(consultations_df['consultation_date'])

    merged_df = pd.merge(customers_df, consultations_df, on='customer_id', how='inner')
    
    # -------------------------------
    # 01. 최근 1달 상담 추이 (분 단위)
    # -------------------------------
    consultations_df['minute_group'] = consultations_df['start_time'].dt.minute // 10 * 10

    result_minute = consultations_df.groupby('minute_group').size().reset_index(name='COUNT')
    result_minute.columns = ['10분대', 'COUNT']

    st.markdown(
        """
        <div style="display:flex; align-items:center;">
            <h3 style="margin:0;">최근 1개월 전체 상담 평균 소요시간 (10분 단위)</h3>
            <span class="tooltip">❔
              <span class="tooltiptext">
                최근 1달 동안 상담이 평균적으로<br>
                얼마나 소요되는지를 10분 단위 구간으로 표시합니다.<br><br>
                이를 통해 예상 대기시간을 가늠하고,<br>
                상담원 인력 배치와 상담 효율성을 개선하는 데<br>
                활용할 수 있습니다.
              </span>
            </span>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.dataframe(result_minute, use_container_width=True)

    # -------------------------------
    # 02.업종별 평균 상담 소요시간
    # -------------------------------
    # 상담 시간(분) 계산
    merged_df['duration_minutes'] = (
        (merged_df['end_time'] - merged_df['start_time']).dt.total_seconds() / 60
    )

    # end_time이 없는 경우 제외
    merged_df = merged_df.dropna(subset=['duration_minutes'])

    # 업종별 평균 상담 시간
    result_duration = merged_df.groupby('business_type')['duration_minutes'].mean().reset_index()
    result_duration = result_duration.rename(columns={'business_type': '업종', 'duration_minutes': '평균 상담시간(분)'})

    # -------------------------------
    # 제목 + 툴팁
    # -------------------------------
    st.markdown(
        """
        <div style="display:flex; align-items:center;">
            <h3 style="margin:0;">업종별 평균 상담 소요시간</h3>
            <span class="tooltip">❔
            <span class="tooltiptext">
                각 업종별 상담의 평균 소요시간(분 단위)을 표시합니다.<br><br>
                예: IT 서비스 업종 평균 35분, 교육 서비스 업종 평균 42분 등
            </span>
            </span>
        </div>
        """,
        unsafe_allow_html=True
    )

    # -------------------------------
    # 그래프 (가로 막대 그래프)
    # -------------------------------
    fig_duration = px.bar(
        result_duration.sort_values("평균 상담시간(분)"),
        x="평균 상담시간(분)",
        y="업종",
        orientation="h",
        labels={"평균 상담시간(분)": "평균 상담시간 (분)", "업종": "업종"},
        color="평균 상담시간(분)",
        color_continuous_scale="Blues",
        text=result_duration["평균 상담시간(분)"].round(1)  # 소수점 1자리까지 표시
    )

    fig_duration.update_traces(textposition="outside")
    fig_duration.update_layout(
        xaxis_title="평균 상담 소요시간 (분)",
        yaxis_title="업종",
        showlegend=False
    )

    st.plotly_chart(fig_duration, use_container_width=True)


    # -------------------------------
    # 2. 최근 1달 상담 추이 (시간대별)
    # -------------------------------
    consultations_df['hour'] = consultations_df['start_time'].dt.hour
    result_hourly = consultations_df.groupby('hour').size().reset_index(name='COUNT')
    result_hourly.columns = ['time', 'COUNT']

    st.markdown(
        """
        <div style="display:flex; align-items:center;">
            <h3 style="margin:0;">최근 1달 상담 추이 (시간대별)</h3>
            <span class="tooltip">❔
            <span class="tooltiptext">
                최근 1달 동안 상담이<br>
                어떤 시간대에 가장 많이 발생했는지 보여줍니다.<br><br>
                상담원 근무시간 최적화에 활용 가능합니다.
            </span>
            </span>
        </div>
        """,
        unsafe_allow_html=True
    )


    custom_scale = [
        [0, "#d4b5ff"],   # 연보라
        [0.5, "#9d6bff"], # 진보라
        [1, "#ff66cc"]    # 핑크 강조
    ]
    
    fig = px.bar(
        result_hourly,
        x='time',
        y='COUNT',
        labels={'time': '시간대 (시)', 'COUNT': '상담 건수 (건)'},
        color='COUNT',
        color_continuous_scale=custom_scale
    )

    # 막대 위 값 표시
    fig.update_traces(text=result_hourly['COUNT'], textposition='outside')

    # 레이아웃 조정
    fig.update_layout(
        xaxis_title="시간대 (시)",
        yaxis_title="상담 건수 (건)",
        showlegend=False
    )

    st.plotly_chart(fig, use_container_width=True)



    # -------------------------------
    # 4. 업종별 상담 건수 분포
    # -------------------------------
    business_count = merged_df.groupby('business_type').size().reset_index(name='상담건수')
    business_count = business_count.sort_values('상담건수', ascending=False)

    st.markdown(
        """
        <div style="display:flex; align-items:center;">
            <h3 style="margin:0;">업종별 상담 건수 분포</h3>
            <span class="tooltip">❔
              <span class="tooltiptext">
                최근 1달 동안 업종별 상담 비중을<br>
                원형 차트로 보여줍니다.<br><br>
                어떤 업종에 집중 대응이 필요한지<br>
                전략 수립에 활용할 수 있습니다.
              </span>
            </span>
        </div>
        """,
        unsafe_allow_html=True
    )
    fig_business = px.pie(
        business_count, values='상담건수', names='business_type',
        color_discrete_sequence=px.colors.qualitative.Pastel
    )
    st.plotly_chart(fig_business, use_container_width=True)

if __name__ == "__main__":
    st.error("이 모듈은 직접 실행할 수 없습니다. main.py를 통해 실행하세요.")
