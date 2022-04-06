# 단순 Echo Server 

from socket import *

serverSock = socket(AF_INET, SOCK_STREAM)    # socket(소켓종류, 소켓유형)
serverSock.bind(('127.0.0.1', 8888))   # 소켓을 주소에 바인딩
serverSock.listen(1) 
print('server start ...')
 
conn, addr = serverSock.accept()
print('client addr: ', addr)
print('from client message: ', conn.recv(1024).decode())
conn.close()
serverSock.close()
 
 
 
 



