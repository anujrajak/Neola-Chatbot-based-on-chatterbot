# vts.py
import speech_recognition as sr

# music.py
import webbrowser
import urllib.request
import urllib.parse
import re
from tts import tts

# news.py
import requests
import json

# tts.py
import pyttsx3

# bot.py
from chatterbot import ChatBot

# mail.py
import imaplib

# weather.py
from weather import Weather, Unit

# scrapping.py
import requests
from bs4 import BeautifulSoup

# Text to speech function
def tts(speak):
	engine = pyttsx3.init()
	engine.setProperty("voice","HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0")
	engine.say(speak)
	engine.runAndWait()


# Voice to invoke
def its():
	try:
		r = sr.Recognizer()
		with sr.Microphone() as source:
			print("----Outside----")
			audio = r.listen(source)
			sound = r.recognize_google(audio)	
			return sound
	except Exception as e:
		print("what was that its")
		# tts("What was that?")	


# Voice to speech
def vts():
	try:
		r = sr.Recognizer()
		with sr.Microphone() as source:
			print("----Inside----")
			audio = r.listen(source)
			sound = r.recognize_google(audio)	
			return sound
	except Exception as e:
		print("what was that ?")
		tts("What was that ?")
	return 0


# Play music from youtube
def music(song):
    # song name from user
    print(song)
    name = urllib.parse.urlencode({"search_query" : song})
    print(name)
    # fetch the ?v=query_string
    result = urllib.request.urlopen("http://www.youtube.com/results?" + name)
    # print(result)
    # make the url of the first result song
    search_results = re.findall(r'href=\"\/watch\?v=(.{11})', result.read().decode())
    # print(search_results)
    # make the final url of song selects the very first result from youtube result
    url = "http://www.youtube.com/watch?v="+search_results[0]
    # play the song using webBrowser module which opens the browser
    webbrowser.open_new(url)


# Read the NEWS
def news():
	url = ('https://newsapi.org/v2/top-headlines?'
		'country=in&'
		'apiKey=ccb51feea28a4433824afe75974301c6')
	response = requests.get(url)
	data = response.json()
	print(data['articles'][0]['title'])
	return data['articles'][0]['title']


# Neola function
def neola(que):
	bot = ChatBot("neola", database="db.sqlite3")
	response = bot.get_response(que)
	print(response)
	return response


# Mail read
def mail():
	imap_host = 'imap.gmail.com'
	imap_user = 'swapnil.tech@global.org.in'
	imap_pass = 'Swapnil@tgs'
	# open a connection
	imap = imaplib.IMAP4_SSL(imap_host)
	# login
	imap.login(imap_user, imap_pass)
	# get status for the mailbox (folder) INBOX
	folderStatus, UnseenInfo = imap.status('INBOX', "(UNSEEN)")
	# print folder Status
	NotReadCounter = str(UnseenInfo[0])
	unread=NotReadCounter.replace("b'\"INBOX\" (UNSEEN ","")
	final=unread.replace(")'","")
	#print(final))
	# print NotReadCounter
	# print "You have "+NotReadCounter+" unread emails"
	mail = "You have "+final+" unread mails."
	print(mail)
	return mail


# Weather Report
def weather(loc='jabalpur'):
	print(loc)
	weather = Weather(unit=Unit.CELSIUS)
	location = weather.lookup_by_location(loc)
	con = location.condition
	report = str("It is a"+con.text+"with "+con.temp+" degree celsius temperature")
	return report


# Search anything
# def srch(que):
# 	print(que)
# 	query = que.replace(" ","+")
#     query = "https://www.google.com/search?q=" + query
#     r = requests.get(query)
#     html_doc = r.text
#     soup = BeautifulSoup(html_doc, 'html.parser')
#     for s in soup.find_all(id="rhs_block"):
#     	print(s.text)	
#     	say = str(s.text)
#     	return say
#     	break

# Wikipedia Search
# def wiki(que):


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
					tts(neola(string))
				elif "neola search" in question:
					string = string.replace("neola search ", "")
					tts(srch(string))
				elif "wikipedia" in question:
					string = string.replace("wikipedia", "")
					tts(wiki(string))
				elif "close" in question:
					break
