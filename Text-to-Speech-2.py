# Import the required module for text to speech conversion
import pyttsx3

# Initialise function to get an engine instance for the speech synthesis
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# say method on the engine that passes input text to be spoken
engine.say('It allows you to easily play mp3 sounds in python, do basic operations on the music and implement callbacks for events like the end of a sound')

# run and wait method, it processes the voice command
engine.runAndWait()