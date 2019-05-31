from lxml import etree
tree = etree.parse("food.xml")

#iter through selected name found in Tree
for element in tree.iter('name'):
    print(element.text)

#iter through selected elements found in Tree
for element in tree.iter('name','rating','feedback'):
    print("{} - {}".format(element.tag, element.text))

