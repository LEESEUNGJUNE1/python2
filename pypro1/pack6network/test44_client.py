# 단순 Client

import socket

clientSock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# clientSock.connect(('192.168.0.10', 7878))
clientSock.connect(('127.0.0.1', 7878))
clientSock.sendall('안녕 서버님'.encode('UTF_8'))
re_msg = clientSock.recv(1024).decode()
print('수신 자료: ', re_msg)
clientSock.close()