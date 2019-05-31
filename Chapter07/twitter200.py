import requests
import json

url = 'https://api.twitter.com/1.1/search/tweets.json?q='

results = requests.get(url)
print("Type Results",type(results))
print("Status Code: ", results.status_code)
print("Headers: Content-Type: ", results.headers['Content-Type'])

#jsonResult = results.json()
jsonResult = results.content
print("Type JSON Results",type(jsonResult))
print(jsonResult)

jsonFinal = json.loads(jsonResult.decode())
print(jsonFinal)
#print(json.loads(requests.get(url).content.decode()))

if results.status_code==400:
    print(jsonFinal['errors'][0]['message'])
else:
    pass
