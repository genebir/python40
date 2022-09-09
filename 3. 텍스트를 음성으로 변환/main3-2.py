from gtts import gTTS
from playsound import playsound

text = "안녕하세요. 염기승승입니아아아아아."

tts = gTTS(text=text, lang="ko")
tts.save(r"hi.mp3")

playsound(r"hi.mp3")