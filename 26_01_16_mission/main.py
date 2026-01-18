# 파이썬 내장 도구 가져오기
from http.server import HTTPServer, BaseHTTPRequestHandler

# 2. 요청을 처리할 점원(Handler) 클래스 만들기
#    (힌트: BaseHTTPRequestHandler를 상속받아야 해요)
class MyHandler(BaseHTTPRequestHandler):
    # GET 요청을 처리하는 함수 정의하기
    def do_GET(self):
        # 1. HTML 조립 (문자열 변수 만들기)
        # 힌트: """ 이용하면 여러 줄의 HTML을 편하게 적을 수 있다.
        # <script>태그 안에 console.log("응답을 받았습니다")를 꼭 넣기.
        html_content = """
        <!DOCTYPE html>
        <html>
        <head><title>Mission 3</title></head>
        <body>
            <h1>서버로부터 응답이 왔습니다!</h1>
            <script>
                // 응답을 받았습니다.
            </script>
        </body>
        </html>
        """

        # 2. 응답 상태 코드 보내기 (성공!)
        self.send_response(200)

        # 3. 응답 헤더 설정 (이건 HTML이고, 한글이 안 깨지게 utf-8이야)
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        # 4. 헤더 작성 끝내기
        self.end_headers()
        # 5. HTML 전송 (문자열을 바이트로 변환해서!)
        message = "<p>나만의 서버</p>"
        self.wfile.write(message.encode('utf-8'))

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