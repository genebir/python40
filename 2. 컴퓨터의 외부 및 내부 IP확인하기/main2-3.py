# 외부 IP알아보기
# 사이트에 접속하기 위해 requests를 설치하여 모듈 불러옴
import requests
# ip주소를 찾기 위한 정규식 사용을 위해 re 모듈을 불러옴
import re

req = requests.get("http://ipconfig.kr")
out_addr = re.search(r' IP Address : (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', req.text)[1]
print(out_addr)
