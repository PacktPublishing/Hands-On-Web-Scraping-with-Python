from lxml import etree
xml = open("food.xml","rb").read()
#tree = etree.fromstring(xml)
#tree = etree.parse(xml)
tree = etree.XML(xml)

print(tree)
print(type(tree))

#iter through all elements found in Tree
for element in tree.iter():
    print("%s - %s" % (element.tag, element.text))

#iter through selected elements found in Tree
for element in tree.iter('price','name'):
    print("%s - %s" % (element.tag, element.text))

#iter through description
for element in tree.iter('description'):
    print("%s - %s" % (element.tag, element.text))

