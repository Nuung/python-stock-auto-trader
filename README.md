# 주식 자동 매도 매수 - 변동성 돌파 전략

> 크레온 API (크레온 PLUS) + python + slack 매도 매수, 

## 참조
- [조코딩 강의](https://youtu.be/Y01D2J_7894)
- [크레온플러스 코드 예제 자료실](https://money2.creontrade.com/e5/mboard/ptype_basic/plusPDS/DW_Basic_List.aspx?boardseq=299&m=9505&p=8833&v=8639)
- [파이썬 증권 데이터 분석](https://github.com/INVESTAR/StockAnalysisInPython)
- [슬랙 메시지 빌더 디자인](https://app.slack.com/block-kit-builder)


## 들어가기 전
- python 3.9 (3.10 은 사용하는 라이브러리 버전 에러)
- only window 32bit (크레온 api 사용하기 위한 조건)


## Start
```bash
# git clone은 패스
# python 가상환경 구축 
python -m venv .venv
cd .venv
Scripts\activate.bat
cd ..
pip install -r requirements.txt

# 최상위 디렉토리에서 
vim .env

# ENV variables
ID="크레온아이디"
PWD="크레온비밀번호"
CERT_PWD="공동인증서비밀번호"
TOKEN="슬랙앱API토큰"

# slack 세팅은 pass - app 만들고 채널 세팅해야함
python __init__.py
```