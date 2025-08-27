# 툭툭 상담사 관리용 대시보드
가상 데이터를 이용해 상담사 관리용 대시보드를 만들었습니다.   


## 사용법   
1. 가상데이터 생성   
streamlit 폴더 안 gen_data.html을 실행시켜 데이터를 다운 받습니다.

2. 가상데이터 Mysql 입력   
다운받은 가상데이터를 data폴더를 생성해 넣은 후 All_connect.ipynb을 실행시켜 MySql에 데이터를 넣습니다.   
- MySQL 정보를 .env파일에 넣어주세요.   

3. FAST API를 이용해 서버 구축   
MYSQL에 insert된 데이터를 확인후 DB폴더 안에 DB_main.py를 실행시키세요.    
CMD에서 python -m DB.DB_main.py 코드 실행    

4. STREAMLIT 대시 보드 구축   
streamlit 폴더안에 main.py를 실행시키세요.    
CMD에서 streamlit run streamlit/main.py 코드 실행   
