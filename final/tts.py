""" 
	This module converts string to voice using PyTtsx3 and win32com module
	* To use it's function just import like this -
		from tts import tts
"""
import pyttsx3
def tts(msg):
	engine = pyttsx3.init()
	rate = engine.getProperty('rate')
	engine.setProperty('rate', rate-60)
	# voices = engine.getProperty('voices')
	# engine.setProperty('voice',voices[1].id)
	engine.setProperty('voice', 'Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')
	engine.say(msg)
	engine.runAndWait()

# tts('say neola')


# engine = pyttsx3.init()
# rate = engine.getProperty('rate')
# engine.setProperty('rate', rate-60)
# voices = engine.getProperty('voices')
# engine.setProperty('voice',voices[1].id)
# engine.say('The quick brown fox jumped over the lazy dog.')
# engine.runAndWait()


