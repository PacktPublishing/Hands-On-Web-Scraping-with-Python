from lxml import etree
xml = open("simple.xml","rb").read()
#tree = etree.fromstring(xml)
#tree = etree.parse(xml)
tree = etree.XML(xml)
for element in tree.iter('name'):
    print("%s - %s" % (element.tag, element.text))

