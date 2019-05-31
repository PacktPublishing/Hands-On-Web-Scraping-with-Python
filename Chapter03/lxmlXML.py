import requests
from lxml import etree
url="https://www.w3schools.com/xml/simple.xml"
response = requests.get(url).content
tree = etree.XML(response)
print(tree)
print(type(tree))
#iter through all elements found in Tree
for element in tree.iter():
    print("%s - %s" % (element.tag, element.text)

#iter through selected elements found in Tree
for element in tree.iter('calories','name'):
    print("%s - %s" % (element.tag, element.text))
