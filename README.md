# colormytree.me-Request
requests 라이브러리를 활용함으로써 WebDriver의 리소스, 처리속도, uncaughtexception 등을 완벽하게 보완하고 작업을 명확하게 처리할 수 있습니다.

## 테스트 환경 구축
사용된 라이브러리 : `asyncio`, `datetime`, `requests`, `json`
파이썬 빌드버전 : `Python 3.8.10 (tags/v3.8.10:3d8993a, May  3 2021, 11:48:03) [MSC v.1928 64 bit (AMD64)] on win32`

```py
user_id = ""  # 트리 유저아이디
content = ""  # 멘트
nickname = ""  # 닉네임
isPrivate = False  # 비공개 여부
```

소스코드 상단부에 위와같은 변수가 위치해있습니다.
트리 유저 아이디란 `https://colormytree.me/2022/01GMGDG8XMF0J7983WPB9S` (`https://colormytree.me/2022/01GMGDG8XMF0J7983WPB9S?page=2`) 중 `01GMGDG8XMF0J7983WPB9S` 를 의미합니다. 

## 테스트
소스
