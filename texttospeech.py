import gtts
import playsound

text="ashii aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"



sound=gtts.gTTS(text=text,lang="en")
sound.save("welcome.mp3")
for i in range(3):
   playsound.playsound("welcome.mp3")