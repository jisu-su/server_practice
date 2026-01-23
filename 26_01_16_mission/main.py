# 파이썬 내장 도구 가져오기
from http.server import HTTPServer, BaseHTTPRequestHandler
# data.py에서 maslow_data 가져오기
from data import maslow_data 
# urllib.parse 쓰기
import urllib.parse

comment_list = []
# 2. 요청을 처리할 점원(Handler) 클래스 만들기
#    (힌트: BaseHTTPRequestHandler를 상속받아야 해요)
class MyHandler(BaseHTTPRequestHandler):
    # GET 요청을 처리하는 함수 정의하기
    def do_GET(self):
        global maslow_data
        # html 파일 불러오기
        with open("index.html", "r", encoding="utf-8") as f:
            index_design = f.read()
        with open("header.html", "r", encoding="utf-8") as f:
            header_design = f.read()
        with open("create_form.html", "r", encoding="utf-8") as f:
            form_design = f.read()

        # 1. [Delete] 삭제 요청 처리
        if "/delete" in self.path:
            try:
                target_id = int(self.path.split("id=")[1])
                maslow_data = [item for item in maslow_data if item['id'] != target_id]
            except:
                pass
            
            # 삭제 후 새로고침 효과 (Location 헤더로 재접속 유도)
            self.send_response(303)
            self.send_header('Location', '/')
            self.end_headers()
            return # 삭제 처리가 끝났으면 여기서 함수 종료!
        
        # [Create] 새로운 단계 추가 로직
        if "/create" in self.path:
                # 1. 주소창에서 정보들 쪼개기, 외계어를 한국어로 해독하기
                # 예: /create?stage=6단계&name=디지털욕구&content=연결되고싶다&example=폰,컴퓨터
                query_string = urllib.parse.unquote_plus(self.path.split("?")[1])

                params = {}
                for param in query_string.split("&"):
                    key, value = param.split("=")
                    params[key] = value
                
                if len(maslow_data) > 0 :
                    new_id = max(item['id'] for item in maslow_data) +1
                else:
                    new_id = 1

                new_data = {
                    "id": new_id,
                    "stage": params['stage'],
                    "name": params['name'],
                    "content": params['content'],
                    "example": params['example']
                }
                # 2. 리스트에 추가 (이게 핵심 Create!)
                maslow_data.append(new_data)

            
                # 3. 추가했으니 다시 메인화면으로!
                self.send_response(303)
                self.send_header('Location', '/')
                self.end_headers()
                return
        
        # [Update] 수정 요청 처리
        if "/edit" in self.path:
            target_id = int(self.path.split("id=")[1])
            for item in maslow_data:
                if target_id == item['id']:

                    with open("edit.html", "r", encoding="utf-8") as f:
                        edit_design = f.read()

                    final_edit_html = edit_design.replace("{{edit_id}}", str(item['id']))
                    final_edit_html = final_edit_html.replace("{{edit_stage}}", item['stage'])
                    final_edit_html = final_edit_html.replace("{{edit_name}}", item['name'])
                    final_edit_html = final_edit_html.replace("{{edit_content}}", item['content'])
                    final_edit_html = final_edit_html.replace("{{edit_example}}", item['example'])

                    self.send_response(200)
                    self.send_header('Content-Type', 'text/html; charset=utf-8')
                    self.end_headers()
                    self.wfile.write(final_edit_html.encode('utf-8'))
                    return
            
        # [Update] 실제로 데이터를 수정하는 로직
        if "/update" in self.path:
                # 1. 주소창 정보 해독
                query = urllib.parse.unquote_plus(self.path.split("?")[1])
                # 2. 정보들을 쪼개서 딕셔너리로 만들기
                params = {}
                for param in query.split("&"):
                    key, value = param.split("=")
                    params[key] = value
                # 주소창에서 id 추출
                target_id = int(params['id'])

                for item in maslow_data:
                    if item['id'] == target_id:
                        item['stage'] = params['stage']
                        item['name'] = params['name']
                        item['content'] = params['content']
                        item['example'] = params['example']
                        break # 찾았으니 더 안 돌고 끝내기

                # 4. 수정 완료 후 메인 화면으로 이동
                self.send_response(303)
                self.send_header('Location', '/')
                self.end_headers()
                return
        
        # stages_html 불러오기
        with open("stages.html", "r", encoding="utf-8") as f:
            stages_design = f.read()

            # 2. 데이터 기반으로 조립되는 부분 (동적)
        stages_html = ""
        for i, item in enumerate(maslow_data):

            delete_button = ""
            if i != 0:
                delete_button = f'<a href="/delete?id={item['id']}" style="color: red;">[삭제하기]</a>'
            
            # 예시 리스트 만드는 로직도 파이썬이 처리
            exams = "".join([f"<li>{ex.strip()}</li>" for ex in item["example"].split(",")])
            exams_html = f"<ul>{exams}</ul>"

            # 읽어온 stages.html 데이터 채우기
            one_stage = stages_design.replace("{{id}}", str(item['id']))
            one_stage = one_stage.replace("{{stage}}", item['stage'])
            one_stage = one_stage.replace("{{name}}", item['name'])
            one_stage = one_stage.replace("{{content}}", item['content'])
            one_stage = one_stage.replace("{{exams}}", exams_html)
            one_stage = one_stage.replace("{{delete_button}}", delete_button)

            #조립된 것들 전체 결과에 넣기
            stages_html += one_stage


        # 구멍 뚫어놓은 곳에 데이터 채우기
        final_html = index_design.replace("{header_html}", header_design)
        final_html = final_html.replace("{create_form_html}", form_design)
        final_html = final_html.replace("{{stages_html}}", stages_html)

        # 2. 응답 상태 코드 보내기 (성공!)
        self.send_response(200)
        # 3. 응답 헤더 설정 (이건 HTML이고, 한글이 안 깨지게 utf-8이야)
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        # 4. 헤더 작성 끝내기
        self.end_headers()
        # 5. HTML 전송 (문자열을 바이트로 변환해서!)
        self.wfile.write(final_html.encode('utf-8'))

    # POST 함수 만들기
    def do_POST(self):
        # 들어온 데이터의 전체 길이가 얼마인지 읽어 오기 
        self.headers.get('Content-Length')
        number_of_letter = int(self.headers.get('Content-Length'))
        # 데이터 꺼내기
        comment = self.rfile.read(number_of_letter)
        # 읽은 데이터를 한글 문자열로 변환
        comments = comment.decode('utf-8')
        # 변환된 문자열에서 실제 필요한 값만 뽑아내어 리스트에 추가 - 필터링
        result = urllib.parse.unquote_plus(comments.split("=")[1])
        comment_list.append(result)

        # 작업이 끝나면 리다이렉트를 사용해 메인 화면으로 돌려보내기
        self.send_response(303)
        self.send_header('Location', '/')
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