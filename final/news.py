import requests
import json
from tts import tts
def news():
    url = ('https://newsapi.org/v2/top-headlines?'
           'country=in&'
           'apiKey=ccb51feea28a4433824afe75974301c6')
    response = requests.get(url)
    data = response.json()
    print("NEWS : "+data['articles'][0]['title'])
    return data['articles'][0]['title']

# print(news())
# tts(news())
