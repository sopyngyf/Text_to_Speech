# Import the required module for text to speech conversion
from gtts import gTTS

#Import module so that can play converted audio
import os

# The text you want to convert to audio
mytext = 'Offset printing prints background design indirectly onto the pages of genuine travel documents. Such method results in smooth, uniform image without embossment. Most importantly, when viewed under the magnifier, good quality, high-resolution print can be observed'

# Language you want to convert the audio to
language = 'en-UK'

# Passing the text and language to the engine, where marked slow=false. This tells the module that the converted audio should have a high speed
myobj = gTTS(text=mytext, lang=language, slow=False)

#Saving the converted audio in a MP3 file named welcome
myobj.save("Test1.mp3")

# Playing the converted file
os.system("mpg321 Test1.mp3")