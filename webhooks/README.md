# JANDI로 메세지 쏴주기

### prerequisite
- JANDI connect에서 webhook incomming 활성화하기
- webhook url 복사해오기
- pip install -r requirements.txt

### reference
- [설명서](https://drive.google.com/file/d/0B2qOhquiLKk0TVBqc2JkQmRCMGM/view)

### demo code
- config.py 생성
	- config.py 내에 WEBHOOK\_URL 변수에 복사한 url을 입력한다
- msg\_push.py

```python
def simple_push(message):
	=> 단순한 message를 보내는 함수
def connect_push(message, **kwargs):
	=> connect라고 불리우는 아이(설명서 참고)도 메세지에 넣기위한 함수
```
