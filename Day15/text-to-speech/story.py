from gtts import gTTS
import os
my_story = 'One day, A boy from small village. who was working hard to become successfull! met a girl XYZ , later their bond becomes very strong. As years past, they married and lived peaceful life. '

generate = gTTS(text=my_story, lang='en', slow = False)
generate.save('mystory.mp3')