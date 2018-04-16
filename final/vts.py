import speech_recognition as sr

def vts():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("say:")
		audio = r.listen(source)
	msg = r.recognize_google(audio)
	return msg

# # # print(vts())

# from pocketsphinx import LiveSpeech
# import time

# msg = ""
# for phrase in LiveSpeech():
# 	msg = msg + str(phrase)
# 	print(msg)
