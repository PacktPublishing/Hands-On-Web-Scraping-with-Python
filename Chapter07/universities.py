import requests
import json
dataSet = []

url = 'http://universities.hipolabs.com/search?name='

def readUrl(search):
    results = requests.get(url+search)
    print("Status Code: ", results.status_code)
    print("Headers: Content-Type: ", results.headers['Content-Type'])
    # print("Headers: ", results.headers)
    return results.json()

if __name__=="__main__":
    jsonResult = readUrl('Wales')
    # print(jsonResult)
    for university in jsonResult:
        name = university['name']
        url = university['web_pages'][0]
        dataSet.append([name,url])

    print("Total Universities Found: ",len(dataSet))
    print(dataSet)

'''
Status Code:  200
Headers: Content-Type:  application/json
Total Universities Found:  10
[['University of Wales', 'http://www.wales.ac.uk/'],
 ['University of Wales Institute, Cardiff', 'http://www.uwic.ac.uk/'], 
 ['University of Wales College of Medicine', 'http://www.uwcm.ac.uk/'], 
 ['Johnson & Wales University', 'http://www.jwu.edu/'], 
 ['University of New South Wales', 'http://www.unsw.edu.au/'], 
 ['University of Wales, Newport', 'http://www.newport.ac.uk/'], 
 ['University of Wales, Swansea', 'http://www.swan.ac.uk/'], 
 ['University of Wales, Aberystwyth', 'http://www.aber.ac.uk/'], 
 ['University of Wales, Lampeter', 'http://www.lamp.ac.uk/'],
  ['University of Wales, Bangor', 'http://www.bangor.ac.uk/']]
'''
