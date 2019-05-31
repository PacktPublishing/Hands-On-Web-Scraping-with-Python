import requests
import json

# location: Kathmandu, Nepal
# lat = 27.717245 , lng=85.323959
url = 'https://api.sunrise-sunset.org/json?lat=27.717245&lng=85.323959&date=2019-03-04'

results = requests.get(url)
print("Type Results",type(results))
print("Status Code: ", results.status_code)
print("Headers: Content-Type: ", results.headers['Content-Type'])
print("Headers: ", results.headers)

jsonResult = results.json()
print("Type JSON Results",type(jsonResult))
print(jsonResult)
print("SunRise & Sunset: ",jsonResult['results']['sunrise']," & ",jsonResult['results']['sunset'])


# Type Results <class 'requests.models.Response'>
# Status Code:  200
# Headers-ContentType:  application/json
# Headers:  {'Access-Control-Allow-Origin': '*', 'Content-Type': 'application/json', 'Vary': 'Accept-Encoding', 'Server': 'nginx', 'Connection': 'keep-alive', 'Content-Encoding': 'gzip', 'Transfer-Encoding': 'chunked', 'Date': 'Mon, 04 Mar 2019 07:48:29 GMT'}
# Type JSON Results <class 'dict'>
# {'status': 'OK', 'results': {'civil_twilight_end': '12:44:16 PM', 'astronomical_twilight_end': '1:38:31 PM', 'civil_twilight_begin': '12:16:32 AM', 'sunrise': '12:39:54 AM', 'nautical_twilight_begin': '11:49:24 PM', 'astronomical_twilight_begin': '11:22:17 PM', 'nautical_twilight_end': '1:11:24 PM', 'sunset': '12:20:54 PM', 'solar_noon': '6:30:24 AM', 'day_length': '11:41:00'}}
# SunRise & Sunset:  12:39:54 AM  &  12:20:54 PM
