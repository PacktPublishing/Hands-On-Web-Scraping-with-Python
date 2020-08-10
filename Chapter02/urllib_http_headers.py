import urllib.request

url='https://www.samsclub.com/sitemap.xml'
someRequest = urllib.request.urlopen(url)#loads provided URL
someRequest.getheaders() #Lists all HTTP headers.
someRequest.getheader("Content-Type") #return value of header 'Content-Type'
