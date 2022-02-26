
# https://finance.daum.net/domestic/etf 참조
# lib
from turtle import st
import requests
from bs4 import BeautifulSoup

# 탑 10 거래량 크롤링해오기, 그리고 종목코드만 가져오기 
def get_etf_list():
    url = "https://finance.daum.net/api/etfs"

    # "fieldName" 값으로 changeRatem(전일대비), accTradeVolume(총거래량)
    querystring = {
        "page":"1",
        "perPage":"30",
        "fieldName":"accTradeVolume",
        "order":"desc",
        "pagination":"true"
    }
    headers = {
        "cookie": "_dfs=ckEzNmFoL1p5WWxuTTdydm1CcDVEU0VIMmtPOGEzQXVWK3hTSm1SaUV3cW5iYUNmQ1YycEEwbTluazkvaHdHT2RKcDhLaGJTZ2lCU2ZaS2hzaGVpd3c9PS0tdXlMOWpDVkxwL25wNEdIN25jVTNudz09--4e2dd00cb94c8bdced588b4323527af3e7103f29",
        "authority": "finance.daum.net",
        "pragma": "no-cache",
        "cache-control": "no-cache",
        "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
        "accept": "application/json, text/javascript, */*; q=0.01",
        "x-requested-with": "XMLHttpRequest",
        "sec-ch-ua-mobile": "?0",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-site": "same-origin",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://finance.daum.net/domestic/etf",
        "accept-language": "en,ko-KR;q=0.9,ko;q=0.8,en-US;q=0.7"
    }

    try:
        res = requests.request("GET", url, headers=headers, params=querystring).json()
        return res
    except Exception as e:
        print(f"get_etf_list error: {e}, {type(e).__name__}, {type(e)}")

    
    
# export function
def get_target_etf(num: int) -> dict:
    stokc_list = get_etf_list()['data']
    return_stokc_dict = {
        "symbol_name": list(),
        "symbol_list": list(),
    }

    for index, stock in enumerate(stokc_list):
        if index > num:
            return return_stokc_dict

        return_stokc_dict['symbol_name'].append(stock['name'])
        return_stokc_dict['symbol_list'].append(stock['symbolCode'])

    return return_stokc_dict

# test
# print(get_target_etf(5))