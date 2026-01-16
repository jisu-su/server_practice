# 파이썬 내장 도구 가져오기
from http.server import HTTPServer, BaseHTTPRequestHandler

# 2. 요청을 처리할 점원(Handler) 클래스 만들기
#    (힌트: BaseHTTPRequestHandler를 상속받아야 해요)
class MyHandler(BaseHTTPRequestHandler):
    # GET 요청을 처리하는 함수 정의하기
    def do_GET(self):
        # 성공 응답(200) 보내기
        # 헤더 마감하기 (내용물은 아직 없어도 돼요)

# 3. 서버 설정 (주소는 'localhost', 포트는 8000)

# 4. 진짜 서버 객체 만들기 
#    (힌트: HTTPServer에게 주소와 점원을 알려주세요)

# 5. 서버 실행 문구 출력하기

# 6. 무한 대기 실행하기 (try-except로 안전하게!)