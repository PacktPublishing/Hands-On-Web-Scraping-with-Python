import requests
url = 'https://api.github.com'

results = requests.get(url)
print("Type Results", type(results))
print("Status Code: ", results.status_code)
print("Headers: Content-Type: ", results.headers['Content-Type'])
print("Headers: ", results.headers)

etag = results.headers['ETag']
print("ETag: ",etag)
results = requests.get(url, headers={'If-None-Match': etag})
print("Type Results", type(results))
print("Status Code: ", results.status_code)
print("Headers: Content-Type: ", results.headers['Content-Type'])
