# Web server : 클라이언트와 통신이 가능
#CGI (Common Gateway Interface)
# : 웹서버와 외부 프로그램 사이에서 정보를 주고 받는 방법이나 규약. 대화형 웹 페이지 작성 가능
# : DB 자료 처리, form tag를 사용한 자료 전송 가능

from http.server import HTTPServer, CGIHTTPRequestHandler # 고객의 정보와 파이썬을 사용하기위해

PORT = 8888

class Handler(CGIHTTPRequestHandler):
    sgi_directories = ['/cgi-bin']

serv = HTTPServer(('127.0.0.1', PORT), Handler) # 127.0.0.1 = 로컬 호스트

print('웹 서비스 시작 ...')

serv.serve_forever() # 서버를 계속 돌리는