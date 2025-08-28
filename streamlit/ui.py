import streamlit as st

def ui_css():
    st.markdown("""
    <style>
        /* 메인 배경 - 부드러운 그라데이션 */
        .stApp {
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        
        /* 왼쪽 파란색 제거 */
        .block-container {
            padding-left: 1rem !important;
            padding-right: 1rem !important;
        }

        .main .block-container {
            max-width: none !important;
            padding-top: 2rem !important;
        }
        
        /* 헤더 스타일 - 깔끔한 디자인 */
        .main-header {
            background: #ffffff;
            padding: 2.5rem 2rem;
            border-radius: 15px;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.08);
            margin-bottom: 2rem;
            text-align: center;
            position: relative;
            overflow: hidden;
        }
        
        .main-header::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 4px;
            background: linear-gradient(90deg, #667eea, #764ba2, #f093fb);
        }
        
        .main-header h1 {
            color: #2c3e50;
            font-size: 2.8rem;
            margin-bottom: 0.5rem;
            font-weight: 700;
            background: linear-gradient(135deg, #667eea, #764ba2);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        
        .main-header p {
            color: #5a6c7d;
            font-size: 1.1rem;
            margin: 0;
            font-weight: 500;
        }
        
        /* 메트릭 카드 스타일 - 색상 포인트와 애니메이션 */
        .metric-card {
            background: #ffffff;
            padding: 2rem;
            border-radius: 12px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
            border: 1px solid #e1e8ed;
            text-align: center;
            transition: all 0.3s ease;
            margin-bottom: 1rem;
            position: relative;
            overflow: hidden;
        }
        
        /* 메트릭 카드 상단 색상 바 */
        .metric-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 4px;
            background: linear-gradient(90deg, #667eea, #764ba2);
            border-radius: 12px 12px 0 0;
            transition: height 0.3s ease;
        }
        
        .metric-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 12px 40px rgba(0, 0, 0, 0.15);
            border-color: #667eea;
        }
        
        .metric-card:hover::before {
            height: 6px;
        }
        
        /* 메트릭별 색상 차별화 */
        .metric-total::before { 
            background: linear-gradient(90deg, #28a745, #20c997); 
        }
        
        .metric-users::before { 
            background: linear-gradient(90deg, #17a2b8, #6f42c1); 
        }
        
        .metric-time::before { 
            background: linear-gradient(90deg, #ffc107, #fd7e14); 
        }
        
        .metric-rate::before { 
            background: linear-gradient(90deg, #fd7e14, #e83e8c); 
        }
        
        .metric-satisfaction::before { 
            background: linear-gradient(90deg, #6f42c1, #6610f2); 
        }
        
        /* 사이드바 스타일 */
        .css-1d391kg {
            background: #ffffff;
            border-right: 2px solid #e1e8ed;
        }
        
        /* 버튼 스타일 - 더 현대적인 디자인 */
        .stButton > button {
            background: linear-gradient(45deg, #667eea, #764ba2);
            color: white;
            border: none;
            border-radius: 12px;
            padding: 0.8rem 2rem;
            font-weight: 600;
            font-size: 1rem;
            transition: all 0.3s ease;
            width: 100%;
            position: relative;
            overflow: hidden;
        }
        
        .stButton > button::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent);
            transition: left 0.5s;
        }
        
        .stButton > button:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 25px rgba(102, 126, 234, 0.3);
            background: linear-gradient(45deg, #5a6fd8, #6a42a0);
        }
        
        .stButton > button:hover::before {
            left: 100%;
        }
        
        /* 선택박스 스타일 */
        .stSelectbox > div > div {
            background: #ffffff;
            border: 2px solid #e1e8ed;
            border-radius: 12px;
            transition: all 0.3s ease;
        }
        
        .stSelectbox > div > div:focus-within {
            border-color: #667eea;
            box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
            transform: translateY(-2px);
        }
        
        /* 데이터프레임 스타일 */
        .dataframe {
            background: #ffffff;
            border-radius: 12px;
            overflow: hidden;
            border: 1px solid #e1e8ed;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);
        }
        
        /* 메트릭 숫자 스타일 - 애니메이션 효과 */
        .metric-value {
            font-size: 3.2rem;
            font-weight: 800;
            color: #2c3e50;
            margin-bottom: 0.5rem;
            line-height: 1.1;
            animation: countUp 1.5s ease-out;
            background: linear-gradient(135deg, #2c3e50, #34495e);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        
        .metric-label {
            font-size: 1.1rem;
            color: #5a6c7d;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            margin-top: 0.5rem;
        }
        
        /* 카운터 애니메이션 */
        @keyframes countUp {
            0% { 
                opacity: 0; 
                transform: translateY(30px) scale(0.8); 
            }
            50% { 
                transform: translateY(-5px) scale(1.05); 
            }
            100% { 
                opacity: 1; 
                transform: translateY(0) scale(1); 
            }
        }
        
        /* 상태 배지 - 더 현대적인 디자인 */
        .status-badge {
            padding: 0.5rem 1rem;
            border-radius: 25px;
            font-size: 0.85rem;
            font-weight: 700;
            display: inline-block;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            position: relative;
            overflow: hidden;
            transition: all 0.3s ease;
        }
        
        .status-active {
            background: linear-gradient(135deg, #28a745, #20c997);
            color: #ffffff;
            box-shadow: 0 4px 15px rgba(40, 167, 69, 0.3);
        }
        
        .status-inactive {
            background: linear-gradient(135deg, #dc3545, #c82333);
            color: #ffffff;
            box-shadow: 0 4px 15px rgba(220, 53, 69, 0.3);
        }
        
        .status-busy {
            background: linear-gradient(135deg, #ffc107, #fd7e14);
            color: #212529;
            box-shadow: 0 4px 15px rgba(255, 193, 7, 0.3);
        }
        
        .status-badge:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(0, 0, 0, 0.2);
        }
        
        /* 차트 컨테이너 스타일 */
        .chart-container {
            background: #ffffff;
            padding: 2rem;
            border-radius: 15px;
            box-shadow: 0 6px 25px rgba(0, 0, 0, 0.08);
            margin-bottom: 2rem;
            border: 1px solid #e1e8ed;
            position: relative;
            overflow: hidden;
        }
        
        .chart-container::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 3px;
            background: linear-gradient(90deg, #667eea, #764ba2, #f093fb);
        }
        
        /* 탭 스타일링 - 대폭 개선 */
        .stTabs [data-baseweb="tab-list"] {
            gap: 8px;
            border-bottom: 2px solid #e1e8ed;
            padding-bottom: 0;
            background: transparent;
        }
        
        .stTabs [data-baseweb="tab"] {
            background: #f8f9fa;
            border-radius: 12px 12px 0 0;
            padding: 1rem 2rem;
            font-weight: 600;
            color: #5a6c7d;
            border: 2px solid #e1e8ed;
            border-bottom: none;
            transition: all 0.3s ease;
            position: relative;
        }
        
        .stTabs [data-baseweb="tab"]:hover {
            background: #ffffff;
            transform: translateY(-2px);
            color: #667eea;
        }
        
        .stTabs [aria-selected="true"] {
            background: #ffffff;
            border-color: #667eea;
            color: #667eea;
            font-weight: 700;
            transform: translateY(-2px);
            box-shadow: 0 4px 15px rgba(102, 126, 234, 0.1);
        }
        
        .stTabs [aria-selected="true"]::after {
            content: '';
            position: absolute;
            bottom: -2px;
            left: 0;
            right: 0;
            height: 3px;
            background: linear-gradient(90deg, #667eea, #764ba2);
        }
        
        /* 반응형 디자인 */
        @media (max-width: 768px) {
            .metric-value {
                font-size: 2.5rem;
            }
            
            .main-header h1 {
                font-size: 2.2rem;
            }
            
            .metric-card {
                padding: 1.5rem;
            }
            
            .stTabs [data-baseweb="tab"] {
                padding: 0.8rem 1.5rem;
                font-size: 0.9rem;
            }
        }
        
        @media (max-width: 480px) {
            .metric-value {
                font-size: 2rem;
            }
            
            .main-header {
                padding: 2rem 1rem;
            }
            
            .main-header h1 {
                font-size: 1.8rem;
            }
        }
        
        /* 텍스트 가독성 개선 */
        .streamlit-expanderHeader {
            font-size: 1.3rem;
            font-weight: 600;
            color: #2c3e50;
            padding: 1rem 0;
        }
        
        /* 로딩 애니메이션 */
        .stSpinner > div > div {
            border-color: #667eea transparent #667eea transparent;
        }
        
        /* 스크롤바 스타일링 */
        ::-webkit-scrollbar {
            width: 8px;
        }
        
        ::-webkit-scrollbar-track {
            background: #f1f1f1;
            border-radius: 10px;
        }
        
        ::-webkit-scrollbar-thumb {
            background: linear-gradient(135deg, #667eea, #764ba2);
            border-radius: 10px;
        }
        
        ::-webkit-scrollbar-thumb:hover {
            background: linear-gradient(135deg, #5a6fd8, #6a42a0);
        }
        
        /* 입력 필드 스타일 */
        .stTextInput > div > div > input {
            border-radius: 12px;
            border: 2px solid #e1e8ed;
            padding: 0.8rem 1rem;
            font-size: 1rem;
            transition: all 0.3s ease;
        }
        
        .stTextInput > div > div > input:focus {
            border-color: #667eea;
            box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
            transform: translateY(-2px);
        }
        
        /* 알림 및 메시지 스타일 */
        .stAlert {
            border-radius: 12px;
            border: none;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
        }
        
        /* 진행률 바 스타일 */
        .stProgress .progress-bar {
            background: linear-gradient(90deg, #667eea, #764ba2);
            border-radius: 10px;
        }
        
        /* 체크박스 스타일 */
        .stCheckbox {
            font-size: 1rem;
            font-weight: 500;
        }
        
        /* 라디오 버튼 스타일 */
        .stRadio {
            font-size: 1rem;
            font-weight: 500;
        }
        
        /* 파일 업로더 스타일 */
        .stFileUploader {
            border: 2px dashed #667eea;
            border-radius: 12px;
            padding: 2rem;
            text-align: center;
            transition: all 0.3s ease;
        }
        
        .stFileUploader:hover {
            border-color: #764ba2;
            background: rgba(102, 126, 234, 0.02);
        }
    </style>
    """, unsafe_allow_html=True)