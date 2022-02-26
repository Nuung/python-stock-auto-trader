
# from https://github.com/INVESTAR/StockAnalysisInPython/blob/master/08_Volatility_Breakout/ch08_01_AutoConnect.py
# 크레온PLUS 자동 접속 프로그램

from pywinauto import application
import time
import os

def auto_conn(id, pwd, cert_pwd):
    os.system('taskkill /IM coStarter* /F /T')
    os.system('taskkill /IM CpStart* /F /T')
    os.system('taskkill /IM DibServer* /F /T')
    os.system('wmic process where "name like \'%coStarter%\'" call terminate')
    os.system('wmic process where "name like \'%CpStart%\'" call terminate')
    os.system('wmic process where "name like \'%DibServer%\'" call terminate')
    time.sleep(5)        

    app = application.Application()
    app.start(f'C:\CREON\STARTER\coStarter.exe /prj:cp /id:{id} /pwd:{pwd} /pwdcert:{cert_pwd} /autostart')
    time.sleep(60)