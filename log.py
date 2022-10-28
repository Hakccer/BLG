from win32com.client import Dispatch
import requests
import json

logc = Dispatch('SAPI.spVoice').Speak

data = requests.get("https://newsapi.org/v2/everything?q=tesla&from=2022-05-09&sortBy=publishedAt&apiKey=90911a1baa3b4909af1dfe41a661c4cb")

result = data.json()
print(result['status'])
print(result)