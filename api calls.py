import requests
import json

# res = requests.get('https://4nieqtfn01.execute-api.ap-south-1.amazonaws.com/Firststage/hanon-services')

# res = requests.get('http://43b4ec7b.ngrok.io/about/sidharth')

dict = {"name": "sidharth", "org": "tcs"}

res1 = requests.post('http://43b4ec7b.ngrok.io/posthandler', json=dict)
print(res1)
