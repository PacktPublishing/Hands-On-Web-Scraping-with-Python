from lxml import etree
tree = etree.parse("simple.xml")
for element in tree.iter('name'):
    print(element.text)
