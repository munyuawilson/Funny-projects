from gtts import gTTS 
import os

text='I am wilson'
object_=gTTS(text,lang='en',slow=False)

object_.save('talkie.mp3')

os.system("mpg123 talkie.mp3")