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
        <head>
            <style>
                body {
                    padding: 40px; /* 전체적으로 40px만큼 안쪽 여백을 줍니다 */
                    line-height: 1.6; /* 줄 간격도 조금 벌려주면 훨씬 읽기 편해요 */
                }
            </style>
            <title>매슬로우의 욕구 이론</title>
        </head>
        <body>
            <h1>매슬로우의 욕구 이론</h1>
            <img src="https://blog.kakaocdn.net/dna/A0sr2/btrNhEwpdg0/AAAAAAAAAAAAAAAAAAAAAHUB9mV9cgjtg96elVmv82Z3iwRSd4iriM1fcF_shscA/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1769871599&allow_ip=&allow_referer=&signature=ArDLQZKX1ZwaQa3z85aSPpbmKG0%3D"
                alt="매슬로우의 욕구 이론 5단계"
                width="400">
            <ul>
                <li>인간의 다양한 욕구가 위계를 갖는다는 심리학적 관점
                <li>인간의 욕구를 생리적 욕구, 안전 욕구, 소속감과 사랑 욕구, 존중 욕구, 자아실현 욕구의 5단계 피라미드로 설명하며,<br>하위 욕구가 충족되어야 상위 욕구를 추구하게 되는 동기 부여 원리이다.
            </ul>
            <h2>1단계: 생리적 욕구 (Physiology)</h2>
            <p>매슬로우 욕구 단계의 기초에 해당하며, 인간 생존을 위한 생물학적 구성 요소이다.</p>
            <ul>
                <li>공기
                <li>물
                <li>음식
                <li>온기
                <li>의복
                <li>생식
                <li>보호소
                <li>수면
            </ul>
            <h2>2단계: 안전의 욕구 (Safety)</h2>
            <p>개인의 생리적 욕구가 충족되면, 다음으로 안전의 용구가 우선하여 행동에 큰 영향을 미친다.
            <br>신체적 안전이 결여된 상황이나 경제적 안전이 결여된 상황에서 나타난다.</p>
            <ul>
                <li>건강
                <li>개인적 안전
                <li>정서적 안전
                <li>재정적 안전
            </ul>
            <h2>3단계: 애정,소속 욕구 (Love/Belonging)</h2>
            <p></p>
            <ul>
                <li>건강
                <li>개인적 안전
                <li>정서적 안전
                <li>재정적 안전
            </ul>
            <script>console.log("응답을 받았습니다.");</script>
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
        self.wfile.write(html_content.encode('utf-8'))

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