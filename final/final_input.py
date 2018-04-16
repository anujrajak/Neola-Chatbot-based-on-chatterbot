# Import all functions
from music import music
from news import news
from tts import tts
from vts import vts
from its import its
from mail import mail
from wea import weather
from bot import  bot
from wiki import wiki


# Infinite Loop
count = 0
while 1:
	tts(mail())
	tts(weather('jabalpur'))
	tts(news())
	while 1:
		string = str(input("Ask -> "))
		if "weather report" in string:
			location = str(input("Enter LOC -> "))
			tts(weather(location))
		elif "news" in string:
			tts(news())
		elif "mail" in string:
			tts(mail())
		elif "song" in string:
			tts("Which song you wanna listen")
			song = str(input("Song -> "))
			music(song)
		elif "neola" in string:
			string = string.replace("neola search ", "")
			tts(bot(string))
		elif "wiki" in string:
			string = string.replace("wiki ", "")
			tts(wiki(string))


