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
            <p>개인의 생리적 욕구가 충족되면, 다음으로 안전의 욕구가 우선하여 행동에 큰 영향을 미친다.
            <br>신체적 안전이 결여된 상황이나 경제적 안전이 결여된 상황에서 나타난다.</p>
            <p>특히 아이들에게서 더 두드러지게 나타나며, 장애를 가진 아이들의 경우 욕구가 더 크다.</p>
            <ul>
                <li>건강
                <li>개인적 안전
                <li>정서적 안전
                <li>재정적 안전
            </ul>
            <h2>3단계: 애정,소속 욕구 (Love/Belonging)</h2>
            <p>생리적 및 안전 욕구가 충족되면, 인간은 대인 관계와 소속감에 대한 욕구를 가진다.</p>
            <p>인간은 크고 작은 사회적 집단에서 소속감과 수용에 대한 정서적 욕구를 가지고 있으며,
            <br>일, 스포츠, 친구 또는 가족과 같은 집단의 일부가 되는 것이 중요하다.</p>
            <p>이 욕구는 특히 어린 시기에 나타나며, 안전 욕구보다도 우선시 될 수 있다.</p>
            <ul>
                <li>가족
                <li>우정
                <li>친밀감
                <li>신뢰
                <li>수용
                <li>사랑과 애정을 주고 받는 것
            </ul>
            <h2>4단계: 존중 욕구 (Esteem)</h2>
            <p>존중은 한 개인에 대한 존경과 감탄을 의미하지만, 동시에 "자존감과 타인의 존중"도 포함된다.</p>
            <p>매슬로우는 존중 욕구를 두 가지 버전으로 나누었다.
            <br>첫 번째는 낮은 단계의 존중 욕구로, 타인으로부터 받는 존중이다.
            <br>두 번째는 높은 단계의 존중 욕구로, 스스로를 존장하는 자존감을 의미한다.</p>
            <ul>
                <li>지위
                <li>명성
                <li>능력
                <li>자신감
                <li>독립
            </ul>
            <h2>5단계: 자아 실현 욕구 (Self-actualization)</h2>
            <p>"사람은 될 수 있는 것은 반드시 되어야 한다" - 에이브러햄 매슬로우</p>
            <p>개인이 자신의 잠재력을 완전히 실현하는 것을 의미한다.
            <br>매슬로우는 모든 것을 이루고, 자신이 될 수 있는 최고의 모습이 되고자 하는 열망이라고 설명한다.</p>
            <ul>
                <li>파트너 찾기
                <li>부모 역할 수행
                <li>재능과 능력의 활용 및 발전
                <li>목표 추고
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