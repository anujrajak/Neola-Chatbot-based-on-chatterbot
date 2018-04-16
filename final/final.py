# Import all functions
from music import music
from news import news
from tts import tts
from vts import vts
from its import its
from mail import mail
from wea import weather
from bot import  bot

# Infinite Loop
count = 0
while 1:
	if count == 0:
		tts(mail())
		tts(weather('jabalpur'))
		tts(news())
		count = 1	
		string = str(its())
		print(string)
		if "hello" in string:
			while 1:
				# tts("ok")
				question = str(vts())
				if "weather report" in question:
					tts("For which location:")
					print("For which location")
					location = str(vts())
					print(location)
					tts(weather(location))
				elif "news" in question:
					tts(news())
				elif "mail" in question:
					tts(mail())
				elif "song" in question:
					tts("which song you wanna listen?")
					song = str(vts())
					print(song)
					name = music(song)
					tts(name)
				elif "say" in question:
					string = string.replace("neola ", "")
					tts(bot(string))
				elif "neola search" in question:
					string = string.replace("neola search ", "")
					tts(srch(string))
				elif "wikipedia" in question:
					string = string.replace("wikipedia", "")
					tts(wiki(string))
				elif "close" in question:
					break
