# socket (컴퓨터가 연결된 접속정보를 받아올 때 사용) 모듈을 불러옴
import socket
# 연결된 소켓의 이름을 가져와 in_addr 변수와 바인딩
in_addr = socket.gethostbyname(socket.gethostname())

print(in_addr)