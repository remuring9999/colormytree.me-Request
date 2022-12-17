# colormytree.me-Request
requests 라이브러리를 활용함으로써 WebDriver의 리소스, 처리속도, uncaughtexception 등을 완벽하게 보완하고 작업을 명확하게 처리할 수 있습니다.

## 목적
**본 소스코드는 교육 및 비영리적 연구를 목적으로 제작되었으며 소스코드 악용시 발생하는 불이익은 모두 본인 책임하에 있습니다**.

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
트리 유저 아이디란  
`https://colormytree.me/2022/01GMGDG8XMF0J7983WPB9S` 
 (`https://colormytree.me/2022/01GMGDG8XMF0J7983WPB9S?page=2`) 중 **`01GMGDG8XMF0J7983WPB9S`** 를 의미합니다. 

## 테스트
소스코드 실행시 **`[성공여부] [현재시각] - [상태코드] | [JSON응답]`** 형식의 로그가 출력됩니다.  
오류 또는 RateLimit 발생시 적절한 조취 또는 소스코드 수정을통해 해결하시면 됩니다.

## 리뷰
500/ms 속도의 Request 요청이 가능합니다.  
테스트 진행중 RateLimit 또는 사이트 접속 불가 / 계정정지 등의 현상은 발생하지 않았습니다.

##Creator
Discord : [! レムリン#9999](http://discord.com/users/863306464915357696)  
Telegram : [@remuring](https://t.me/remuring)

## License
**Code released under the [GNU General Public License version 3.0](https://www.gnu.org/licenses/gpl-3.0.en.html).**
