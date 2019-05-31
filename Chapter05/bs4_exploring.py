from bs4 import BeautifulSoup,SoupStrainer
import re
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
<h1>Secret agents</h1>
<ul>
    <li data-id="10784">Jason Walters, 003: Found dead in "A View to a Kill".</li>
    <li data-id="97865">Alex Trevelyan, 006: Agent turned terrorist leader; James' nemesis in "Goldeneye".</li>
    <li data-id="45732">James Bond, 007: The main man; shaken but not stirred.</li>
</ul>
</body>
</html>
"""
tagsA = SoupStrainer("a")
soupA = BeautifulSoup(html_doc,'lxml',parse_only=tagsA)
soup = BeautifulSoup(html_doc,'lxml')

print(type(soupA))
print(soupA)

print(soupA.prettify())

print(soupA.a.has_attr('class'))

print(soupA.a.has_attr('name'))

print(soupA.find("a")) #print(soupA.find(name="a"))

print(soupA.find("a",attrs={'class':'sister'}))

print(soupA.find("a",attrs={'class':'sister'},text="Lacie"))

print(soupA.find("a",attrs={'id':'link3'}))

print(soupA.find('a',id="link2"))

print(soupA.find_all("a")) 

#find all <a>, but return only 2 of them
print(soupA.find_all("a",limit=2)) #attrs, text

print(soupA.find("a",text=re.compile(r'cie'))) #import re

print(soupA.find_all("a",attrs={'id':re.compile(r'3')}))

print(soupA.find_all(re.compile(r'a')))

#soup
soup = BeautifulSoup(html_doc,'lxml')

print(soup.find_all("p","story")) #class=story

print(soup.find_all("p","title")) #soup.find_all("p",attrs={'class':"title"})

print(soup.find_all("p",attrs={'class':["title","story"]}))

print(soup.find_all(["p","li"]))

print(soup.find_all(string="Elsie")) #text="Elsie"

print(soup.find_all(text=re.compile(r'Elsie'))) #import re

print(soup.find_all("a",string="Lacie")) #text="Lacie"

for li in soup.ul.find_all('li'):
    print(li.name, ' > ',li.get('data-id'),' > ', li.text)

print(soupA.a) #tag a

print(soup.li) #tag li

print(soup.p)

print(soup.p.b) #tag p and b

print(soup.ul.find('li',attrs={'data-id':'45732'}))

print(soup.ul.find('li',attrs={'data-id':'45732'}).text)

print(soup.p.text) #get_text()

print(soup.li.text)

print(soup.p.string)

print(list(soup.find('p','story').children))

print(list(soup.find('p','story').contents))

print(list(soup.find('p','story').descendants))

#using List Comprehension Technique
print([a.name for a in soup.find('p','story').children])

print([{'tag':a.name,'text':a.text,'class':a.get('class')} for a in soup.find('p','story').children if a.name!=None])

print([a.name for a in soup.find('p','story').descendants])

print(list(filter(None,[a.name for a in soup.find('p','story').descendants])))

print(soup.find('p','story').findChildren())

print(soup.find('p','story').findChild()) #soup.find('p','story').find()

#print parent element of <a> with class=sister
print(soup.find('a','sister').parent)

#print parent element name of <a> with class=sister
print(soup.find('a','sister').parent.name)

#print text from parent element of <a> with class=sister
print(soup.find('a','sister').parent.text)

for element in soup.find('a','sister').parents:
    print(element.name)
	
#find single Parent for selected <a> with class=sister 
print(soup.find('a','sister').findParent())

#find Parents for selected <a> with class=sister 
print(soup.find('a','sister').findParents())

print(soup.find('p','story').next)

print(soup.find('p','story').next.next)

print(soup.find('p','story').next_element)

print(soup.find('p','story').next_element.next_element)

print(soup.find('p','story').next_element.next_element.next_element)

print(soup.find('p','story').previous) #returns empty or new-line. 
print(soup.find('p','title').next.next.next) #returns empty or newline similar to code above

print(soup.find('p','story').previous.previous)

print(soup.find('p','story').previous_element) #returns empty or new-line. 
print(soup.find('p','story').previous_element.previous_element)


print(soup.find('p','story').previous_element.previous_element.previous_element)

print(soup.find('p','title').next.next.previous.previous)

for element in soup.find('ul').next_elements:
    print(element)
	
print(soup.find('p','story').next)

print(soup.find('p','story').next_element)

print(soup.find('p','story').find_next()) #element after next_element

print(soup.find('p','story').find_next('h1'))

print(soup.find('p','story').find_all_next())

print(soup.find('p','story').find_all_next('li',limit=2))

print(soup.find('ul').previous.previous.previous)

print(soup.find('ul').find_previous())

print(soup.find('ul').find_previous('p','title'))

print(soup.find('ul').find_all_previous('p'))

print(soup.find('p','title').next_sibling) #returns empty or new-line

print(soup.find('p','title').next_sibling.next_sibling) #print(soup.find('p','title').next_sibling.next)

print(soup.find('ul').previous_sibling) #returns empty or new-line

print(soup.find('ul').previous_sibling.previous_sibling)

#using List Comprehension 
title = [ele.name for ele in soup.find('p','title').next_siblings]
print(list(filter(None,title)))

ul = [ele.name for ele in soup.find('ul').previous_siblings]
print(list(filter(None,ul)))

#find next <p> siblings for selected <p> with class=title
print(soup.find('p','title').find_next_siblings('p'))

#find single or next sibling for selected <h1>
print(soup.find('h1').find_next_sibling())

#find single or next sibling <li> for selected <h1>
print(soup.find('h1').find_next_sibling('li'))

#find first previous sibling to <ul>
print(soup.find('ul').find_previous_sibling())

#find all previous siblings to <ul>
print(soup.find('ul').find_previous_siblings())

#using CSS Selectors
print(soup.select('li[data-id]'))
print(soup.select('ul li[data-id]')[1]) #fetch index 1 only from resulted List
print(soup.select_one('li[data-id]'))
print(soup.select('p.story > a.sister'))#Selects all <a> with class='sister' that are direct child to <p> with class="story"

print(soup.select('p b'))#Selects <b> inside <p>

print(soup.select('p + h1'))#Selects immediate <h1> after <p>

print(soup.select('p.story + h1'))#Selects immediate <h1> after <p> with class 'story'

print(soup.select('p.title + h1'))#Selects immediate <h1> after <p> with class 'title'

print(soup.select('a[href*="example.com"]'))

print(soup.select('a[id*="link"]'))