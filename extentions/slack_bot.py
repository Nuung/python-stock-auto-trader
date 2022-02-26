
# python lib
import os, json, requests
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.environ.get("TOKEN")

def post_message(channel, text, is_block=False, block_data=None):
    # pre setting
    headers = { "Authorization": "Bearer "+ TOKEN }

    if is_block:
        data = {
            "channel": channel,
            "blocks": json.dumps([
                {
                    "type": "header",
                    "text": {
                        "type": "plain_text",
                        "text": "자동 주식 매매 시작합니다.",
                        "emoji": True
                    }
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": f"> 시작 시간 {datetime.now().strftime('[%m/%d %H:%M:%S]')}"
                    }
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": f"종목: {block_data['symbol_list']}"
                    }
                }
            ])
        }
    else:
        data = {
            "channel": channel,
            "text": text
        }

    try:
        res = requests.post("https://slack.com/api/chat.postMessage",
            headers=headers,
            data=data
        )
        if res.status_code != 200:
            raise Exception(f"res.status_code != 200: {res.status_code}")
    except Exception as e:
        print(e)

    # print(response.json())
    # print(response)
 

# post_message("#stock-auto-log","test")