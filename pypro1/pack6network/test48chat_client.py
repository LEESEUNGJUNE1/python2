# 멀티 채팅 클라이언트 : socket, thread

import socket
import threading
import sys

def handle(socket):  
    while True:
        data = socket.recv(1024)
        if not data:continue
        print(data.decode('UTF_8'))

sys.stdout.flush()  # 파이썬의 표준 출력은 버퍼링이 된다.(쌓인다)

name = input('채팅명 입력:')
cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cs.connect(('127.0.0.1',5555))
cs.send(name.encode('UTF_8'))

th = threading.Thread(target=handle, args = (cs,))
th.start()

while True:
    msg = input()   #채팅 메세지(수다) 입력 
    sys.stdout.flush()
    if not msg:continue # 메세지를 입력했으면 send
    cs.send(msg.encode('UTF_8'))

cs.close()















