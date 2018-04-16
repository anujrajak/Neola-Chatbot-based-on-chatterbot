import wikipedia
# keyword = input("Search wikipedia:")
# print(wikipedia.summary(keyword))

def wiki(msg):
		res = wikipedia.summary(msg)
		print(res)
		return res

# wiki("gamcha")