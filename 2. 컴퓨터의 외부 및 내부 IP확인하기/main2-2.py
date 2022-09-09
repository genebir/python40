# main2-1보다 조금 더 정확하게 IP를 확인하는 방법
import socket

# socket연결
in_addr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# google에 접속, https의 기본 접속 포트는 443
in_addr.connect(("www.google.co.kr", 443))
# 연결된 소켓의 이름을 출력, Tuple형태이기 때문에 0번째를 출력
print(in_addr.getsockname()[0])