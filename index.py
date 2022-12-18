import asyncio
import datetime
import requests
import json

user_id = ""  # 트리 유저아이디
content = ""  # 멘트
nickname = ""  # 닉네임
isPrivate = False  # 비공개 여부

async def main(user_id, content, nickname, isPrivate):
    payload = json.dumps({
        "cardMessage": str(content),
        "cardNickname": str(nickname),
        "isPrivateMessage": bool(isPrivate),
        "ornamentId": "1"
    })

    headers = {
        'authority': 'api.colormytree.me',
        'origin': 'https://colormytree.me',
        'referer': 'https://colormytree.me/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Whale/3.18.154.7 Safari/537.36',
        'Content-Type': 'application/json-patch+json'
    }

    while 1:
        try:
            req = requests.post(f"https://api.colormytree.me/users/{user_id}/gifts", headers=headers, data=payload)
            json_ = req.json()
            if req.status_code == 200:
                print(
                    f'Success {datetime.datetime.now()} - {req.status_code} | {json_}')
                await asyncio.sleep(0.5)
            else:
                print(
                    f'Error {datetime.datetime.now()} - {req.status_code} | {json_}')
                await asyncio.sleep(0.5)

        except Exception as e:
            print(f'Error {datetime.datetime.now()} {e}')
            continue

if __name__ == "__main__":
    asyncio.run(main(user_id, content, nickname, isPrivate))
