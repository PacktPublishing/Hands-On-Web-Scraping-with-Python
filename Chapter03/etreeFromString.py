from lxml import html
import requests
response = requests.get('http://httpbin.org/forms/post')
print(type(response.text))
# build the DOM Tree
tree = html.fromstring(response.text)
print(type(tree))
for element in tree.iter('input'):
    print("Element: %s \n\tvalues(): %s \n\tattrib: %s \n\titems(): %s \n\tkeys(): %s"%
        (element.tag, element.values(),element.attrib,element.items(),element.keys()))
    print("\n")

