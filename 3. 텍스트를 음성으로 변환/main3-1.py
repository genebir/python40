# 문자를 음성으로 변환해주는 gtts 모듈 설치
# mp3를 파이썬에서 재생하는 playgsound 모듈 설치
# gtts 라이브러리에서 gTTS만 불러와 사용
from gtts import gTTS

text = "안녕하세요, 염기승 입니다."

tts = gTTS(text=text, lang='ko')
tts.save(r"hi.mp3")