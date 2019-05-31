import urllib.request as request
import urllib.error as error
try:
    request.urlopen("https://www.python.ogr")
except error.URLError as e:
    print("Error Occurred: ",e.reason)
