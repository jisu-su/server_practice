# 파이썬 내장 도구 가져오기
from http.server import HTTPServer, BaseHTTPRequestHandler

# 2. 요청을 처리할 점원(Handler) 클래스 만들기
#    (힌트: BaseHTTPRequestHandler를 상속받아야 해요)
class MyHandler(BaseHTTPRequestHandler):
    # GET 요청을 처리하는 함수 정의하기
    def do_GET(self):
        # 1. 일단 받은 것부터 터미널에 뿌려서 확인하기 (가장 먼저!)
        print("--- 요청 시작 ---")
        # 요청의 첫 번째 줄(Request Line) 출력하기
        # -> self.requestline 이라는 변수에 담겨 있어요.
        print(f"요청 라인: {self.requestline}")
        # 요청 헤더(Headers) 출력하기
        # -> self.headers 라는 변수를 print 해보세요.
        print(f"헤더 내용:\n{self.headers}")
        print("--- 요청 끝 ---")
        # 2. 그다음에 손님에게 응답 보내기
        # 성공 응답(200) 보내기
        self.send_response(200)
        # 헤더 마감하기 (내용물은 아직 없어도 돼요)
        self.end_headers()

# 3. 서버 설정 (주소는 'localhost', 포트는 8000)
host = "localhost"
port = 8000

# 4. 진짜 서버 객체 만들기 
#    (힌트: HTTPServer에게 주소와 점원을 알려주세요)
server = HTTPServer((host,port),MyHandler)

# 5. 서버 실행 문구 출력하기
print("서버가 시작되었습니다")

# 6. 무한 대기 실행하기 (try-except로 안전하게!)
try:
    server.serve_forever()
except KeyboardInterrupt:
    server.server_close()