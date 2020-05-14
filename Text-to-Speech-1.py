# Import the required module for text to speech conversion 
from gtts import gTTS

# Import module to play the converted audio
import os

# Language you want to convert the audio to
language = 'en-US'

# ----------------------- THE TEXT YOU WANT TO CONVERT ---------------------------- #

# The text you want to convert to audio
mytext = 'Opera refers to a dramatic art form, originating in Europe, in which the emotional content is conveyed to the audience as much through music, both the vocal and instrumental, as it is through the lyrics. By contrast, in musical theatre an actors dramatic performance is primary, and the music plays a lesser role. The drama in opera is presented using the primary elements of theatre such as scenery, costumes, and acting. However, the words of the opera, or libretto, are sung rather than spoken. The singers are accompanied by a musical ensemble ranging from a small instrumental ensemble to a full symphonic orchestra.'

# ----------------------- TELLING THE SCRIPT TO RUN ---------------------------- #

# Passing the text and language to the engine, where slow=false. 
# This tells the module that the converted audio should have a high speed
myobj = gTTS(text=mytext, lang=language, slow=False)

# ----------------------- REPLACE TEST1 WITH THE FILE NAME YOU WANT ------------------------- #

#Saving the converted audio in a MP3 file named welcome
myobj.save("Test1.mp3")

# Playing the converted file
os.system("mpg321 Test1.mp3")