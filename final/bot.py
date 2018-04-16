from tts import tts
from chatterbot import ChatBot

def bot(msg):
	bot = ChatBot("neola", database="db.sqlite3")
	res = bot.get_response(msg)
	print('Neola : ', res)
	return res

# tts(bot('hello'))