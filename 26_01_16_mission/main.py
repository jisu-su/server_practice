# 파이썬 내장 도구 가져오기
from http.server import HTTPServer, BaseHTTPRequestHandler
# data.py에서 maslow_data 가져오기
from data import maslow_data 
# urllib.parse 쓰기
import urllib.parse

# 2. 요청을 처리할 점원(Handler) 클래스 만들기
#    (힌트: BaseHTTPRequestHandler를 상속받아야 해요)
class MyHandler(BaseHTTPRequestHandler):
    # GET 요청을 처리하는 함수 정의하기
    def do_GET(self):
        # 1. [Delete] 삭제 요청 처리
        if "/delete" in self.path:
            try:
                index = int(self.path.split("id=")[1])
                del maslow_data[index]
            except:
                pass
            
            # 삭제 후 새로고침 효과 (Location 헤더로 재접속 유도)
            self.send_response(303)
            self.send_header('Location', '/')
            self.end_headers()
            return # 삭제 처리가 끝났으면 여기서 함수 종료!
        
        # [Create] 새로운 단계 추가 로직
        if "/create" in self.path:
            try:
                # 1. 주소창에서 정보들 쪼개기
                # 예: /create?stage=6단계&name=디지털욕구&content=연결되고싶다&example=폰,컴퓨터
                query_string = self.path.split("?")[1]
                # 외계어를 한국어로 해독하기
                query_string = urllib.parse.unquote_plus(query_string)
                params = query_string.split("&")
                
                # 각 정보를 딕셔너리로 조립하기 위해 데이터 추출
                new_data = {}
                for param in params:
                    key, value = param.split("=")
                    new_data[key] = value
                
                # 2. 리스트에 추가 (이게 핵심 Create!)
                maslow_data.append(new_data)
                
            except:
                pass
            
            # 3. 추가했으니 다시 메인화면으로!
            self.send_response(303)
            self.send_header('Location', '/')
            self.end_headers()
            return
        
        # [Update] 수정 요청 처리
        if "/edit" in self.path:
            index = int(self.path.split("id=")[1])
            item = maslow_data[index]
        
            edit_html = f"""
            <h2>단계 수정하기</h2>
            <form action="/update" method="GET">
                <input type="hidden" name="id" value="{index}">

                <p>단계: <input type="text" name="stage" value="{item['stage']}"></p>
                <p>이름: <input type="text" name="name" value="{item['name']}"></p>

                <p>
                    <label style="vertical-align: top;">내용:</label>
                    <textarea name="content" style="vertical-align: top; resize: none; width: 400px; height: 100px;">{item['content']}</textarea>
                </p>

                <p>
                    <label style="vertical-align: top;">예시:</label>
                    <textarea name="example" style="vertical-align: top; resize: none; width: 400px; height: 60px;">{item['example']}</textarea>
                </p>

                <button type="submit" style="padding: 10px 20px; background-color: #4CAF50; color: white; border: none; cursor: pointer;">수정 완료</button>
            </form>
            <a href="/">취소</a>
            """

            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(edit_html.encode('utf-8'))
            return
        
        # [Update] 실제로 데이터를 수정하는 로직
        if "/update" in self.path:
            try:
                # 1. 주소창 정보 해독
                query = urllib.parse.unquote_plus(self.path.split("?")[1])
                # 2. 정보들을 쪼개서 딕셔너리로 만들기
                params = {}
                for param in query.split("&"):
                    key, value = param.split("=")
                    params[key] = value
                # 3. 해당 번호(index)의 데이터를 새 내용으로 교체!
                idx = int(params['id'])
                maslow_data[idx] = {
                    'stage': params['stage'],
                    'name': params['name'],
                    'content': params['content'],
                    'example': params['example']
                }
            except:
                pass

            # 4. 수정 완료 후 메인 화면으로 이동
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

        # Create를 위한 입력 양식 
        create_form_html = """
        <div style="background-color: #f9f9f9; padding: 20px; border: 2px dashed #ccc; margin-bottom: 30px;">
            <h3>새로운 욕구 단계 등록하기</h3>
            <form action="/create" method="GET">
                <input type="text" name="stage" placeholder="예: 6단계" style="width: 100px;">
                <input type="text" name="name" placeholder="욕구 이름 (예: 와이파이 욕구)">
                <br><br>
                <textarea name="content" placeholder="이 욕구에 대한 설명을 적어주세요" style="width: 100%; height: 60px; resize: none;"></textarea>
                <br><br>
                <input type="text" name="example" placeholder="예시 (예: 5G, 무료 와이파이)" style="width: 100%;">
                <br><br>
                <button type="submit" style="background-color: #4CAF50; color: white; padding: 10px 20px; border: none; cursor: pointer;">
                    피라미드에 추가하기</button>
            </form>
        </div>
        """
            # 2. 데이터 기반으로 조립되는 부분 (동적)
        stages_html = ""
        for i, item in enumerate(maslow_data):

            delete_button = ""
            if i != 0:
                delete_button = f'<a href="/delete?id={i}" style="color: red;">[삭제하기]</a>'
            
            exams = ""
            for ex in item["example"].split(","):
                exams += f"<li>{ex.strip()}</li>" 
            exams = f"<ul>{exams}</ul>"
            stages_html += f"""
            <div style="border: 1px solid #ddd; padding: 10px; margin-bottom: 10px;">
                <h2>{item['stage']}: {item['name']}</h2>
                <p>{item['content']}</p>
                <p><strong>예시: {exams}</strong></p>
                {delete_button}
                <a href="/edit?id={i}" style="color: blue; margin-left: 10px;">[수정하기]</a>
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
            {create_form_html}
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