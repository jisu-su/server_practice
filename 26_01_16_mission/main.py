# 파이썬 내장 도구 가져오기
from http.server import HTTPServer, BaseHTTPRequestHandler
# data.py에서 maslow_data 가져오기
from data import maslow_data 

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
                <li>인간의 다양한 욕구가 위계를 갖는다는 심리학적 관점</li>
                <li>인간의 욕구를 생리적 욕구, 안전 욕구, 소속감과 사랑 욕구, 존중 욕구, 자아실현 욕구의 5단계 피라미드로 설명하며,<br>하위 욕구가 충족되어야 상위 욕구를 추구하게 되는 동기 부여 원리이다.</li>
            </ul>
            <hr>
            """
            # 2. 데이터 기반으로 조립되는 부분 (동적)
        stages_html = ""
        for item in maslow_data:
            stages_html += f"""
            <h2>{item['stage']},: {item['name']}</h2>
            <p>{item['content']}</p>
            <ul>
                <li>예시: {item['example']}</li>
            </ul>
            """

            <hr>
            <h1>욕구 이론에 대한 나의 생각</h1>
            <p>매슬로우 욕구 이론은 5단계로 나누어져 하위 욕구를 채워야만 상위 욕구로 나아갈 수 있다는 것이다. 
            <br>욕구를 나눈 큰 틀에 있어서는 많은 부분 동의한다. 그리고 생리적 욕구가 무조건 기초, 첫번째가 되어야 한다는 것도 전적으로 동의한다. 하지만 이 이론이 나온 것이 1940년대인 것을 생각하면 역시 현대와는 맞지 않다고 생각한다. 
            <br>이 이론을 읽으면서 한 가지 생각이 났다. 불우한 환경에서 자란 사람들 중 몇 몇은 자신의 환경을 벗어나기 위해서 엄청난 노력을 한다. 내 생각에 그 사람들은 안전 욕구, 애정·소속 욕구, 존중 욕구에 대해서는 충분한 만족감을 느끼지 못 할 것이다. 그럼에도 그들은 환경을 벗어나려는 결핍 욕구와 그 속에서 성공하려는 자신의 자아 실현 욕구가 동시에 발현된다. 
            <br>현 시대에서 분명한 것은 욕구가 한 단계, 한 단계 일어나는 것이 아닌 피라미드와 상관 없이 복합적으로 일어난다는 것이다. 또한 본인의 욕구로 우선 순위가 바뀌기도 한다. 요즘 안전을 포기하고, 남들의 시선을 신경 쓰지 않고 본인의 자아 실현만을 위해 행동하는 사람들을 찾아 보기 정말 쉽다. 
            <br>이처럼 매슬로우의 욕구 이론은 현대와 어울린다고 하기에는 조금 무리가 있다.</p>
            <hr>
            <h2>출처</h2>
            <p>이미지 출처: <a href="https://pals.tistory.com/2523" target="_blank">티스토리 바로가기</a></p>
            <p>내용 출처: <a href="https://ko.wikipedia.org/wiki/%EB%A7%A4%EC%8A%AC%EB%A1%9C%EC%9D%98_%EC%9A%95%EA%B5%AC%EB%8B%A8%EA%B3%84%EC%9D%B4%EB%A1%A0" target="_blank">위키백과 바로가기</a></p>
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