import requests
import os
link = "https://en.wikipedia.org/wiki/List_of_most_popular_websites"
response = requests.get(link)
content = response.content
file = open(os.getcwd()+os.sep+"tests"+os.sep+"wikicontent.html","wb")
file.write(content)
file.close()
#print(content)  
