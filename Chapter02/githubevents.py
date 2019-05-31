import requests
import os
import json
link = "https://feeds.citibikenyc.com/stations/stations.json" 
# link = "https://api.github.com/events"
response = requests.get(link).json()
print(response['stationBeanList'][0])
# jsonData = json.dumps(response)
# print(type(jsonData))
# print(response[0])

# file = open(os.getcwd()+os.sep+"tests"+os.sep+"github_event.json","w")
# file.write(jsonData)
# file.close()