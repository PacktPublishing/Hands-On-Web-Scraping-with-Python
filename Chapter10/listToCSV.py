import csv
import json

colNames = ['Title','Price','Stock','Rating']
dataSet = [
    ['Rip it Up and ...', 35.02, 'In stock', 5],
    ['Our Band Could Be ...', 57.25, 'In stock', 4],
    ['How Music Works', 37.32, 'In stock', 2],
    ['Love Is a Mix ...', 18.03, 'Out of stock',1],
    ['Please Kill Me: The ...', 31.19, 'In stock', 4],
    ["Kill 'Em and Leave: ...", 45.0, 'In stock',5],
    ['Chronicles, Vol. 1', 52.60, 'Out of stock',2],
    ['This Is Your Brain ...', 38.4, 'In stock',1],
    ['Orchestra of Exiles: The ...', 12.36, 'In stock',3],
    ['No One Here Gets ...', 20.02, 'In stock',5],
    ['Life', 31.58, 'In stock',5],
    ['Old Records Never Die: ...', 55.66, 'Out of Stock',2],
    ['Forever Rockers (The Rocker ...', 28.80, 'In stock',3]
]

print(dataSet)

fileCsv = open('bookdetails.csv', 'w', newline='', encoding='utf-8')
writer = csv.writer(fileCsv)
writer.writerow(colNames)
for data in dataSet:
    writer.writerow(data)
fileCsv.close()


finalDataSet=list() #empty Dataset
for data in dataSet:
    print(dict(zip(colNames,data)))
    finalDataSet.append(dict(zip(colNames,data)))
print(finalDataSet)

with open('bookdetails.json', 'w') as jsonfile:
    json.dump(finalDataSet,jsonfile)


with open('bookdetails.json', 'r+') as jsonfile:
    data = json.load(jsonfile)
    print(data)
    print(data[0])
    print(data[0]['id'])
    print(data[0]['price'])
    print(data[0:2])
