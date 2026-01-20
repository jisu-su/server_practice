# 파이썬 내장 도구 가져오기
from http.server import HTTPServer, BaseHTTPRequestHandler
# data.py에서 maslow_data 가져오기
from data import maslow_data 

# 2. 요청을 처리할 점원(Handler) 클래스 만들기
#    (힌트: BaseHTTPRequestHandler를 상속받아야 해요)
class MyHandler(BaseHTTPRequestHandler):
    # GET 요청을 처리하는 함수 정의하기
    def do_GET(self):
        # 만약 주소에 /delete 가 포함되어 있다면?
        if "/delete" in self.path:
        # 주소창에서 id=번호 부분만 잘라내기 (간단한 예시)
            try:
                index = int(self.path.split("id=")[1])
                del maslow_data[index] # 데이터 삭제! (Delete)
            except:
                pass
        
        # 삭제 후 다시 메인 화면으로 돌려보내기 (새로고침 효과)
        self.send_response(303)
        self.send_header('Location', '/')
        self.end_headers()
        return
        # 1. 고정된 상단 부분 (이미지 및 서론)
        header_html = """
        <h1>매슬로우의 욕구 이론</h1>
        <img src="https://blog.kakaocdn.net/dna/A0sr2/btrNhEwpdg0/AAAAAAAAAAAAAAAAAAAAAHUB9mV9cgjtg96elVmv82Z3iwRSd4iriM1fcF_shscA/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1769871599&allow_ip=&allow_referer=&signature=ArDLQZKX1ZwaQa3z85aSPpbmKG0%3D"
            alt="매슬로우의 욕구 이론 5단계"
            width="400">
        <ul>
            <li>인간의 다양한 욕구가 위계를 갖는다는 심리학적 관점</li>
            <li>인간의 욕구를 생리적 욕구, 안전 욕구, 소속감과 사랑 욕구, 존중 욕구, 자아실현 욕구의 5단계 피라미드로 설명하며,<br>
            하위 욕구가 충족되어야 상위 욕구를 추구하게 되는 동기 부여 원리이다.</li>
        </ul>
        <hr>
        """
            # 2. 데이터 기반으로 조립되는 부분 (동적)
        stages_html = ""
        for i, item in enumerate(maslow_data):
            stages_html += f"""
            <div style="border: 1px solid #ddd; padding: 10px; margin-bottom: 10px;">
                <h2>{item['stage']}: {item['name']}</h2>
                <p>{item['content']}</p>
                <p><strong>예시: </strong>{item['example']}</p>
                <a href="/delete?id={i}" style="color: red;">[이 단계 삭제하기]</a>
            </div>
            """

        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <title>매슬로우의 욕구 이론</title>
            <style>
                body {{
                    padding: 40px; /* 전체적으로 40px만큼 안쪽 여백을 줍니다 */
                    line-height: 1.6; /* 줄 간격도 조금 벌려주면 훨씬 읽기 편해요 */
                }}
            </style>
        </head>
        <body>
            {header_html}
            {stages_html}
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