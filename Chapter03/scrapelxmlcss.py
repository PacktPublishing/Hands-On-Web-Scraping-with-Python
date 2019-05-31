from lxml import html
import requests
from lxml.cssselect import CSSSelector

url = 'https://developer.ibm.com/announcements/category/data-science/?fa=date%3ADESC&fb='
url_get = requests.get(url)
tree = html.document_fromstring(url_get.content)
print(type(tree))

announcements=[]
articles = tree.cssselect('.ibm--card > a.ibm--card__block_link')
for article in articles:

    link = article.get('href')
    atype = article.cssselect('div.ibm--card__body > h5')[0].text.strip()
    adate = article.cssselect('div.ibm--card__body > h5 > .ibm--card__date')[0].text
    title = article.cssselect('div.ibm--card__body > h3.ibm--card__title')[0].text_content()
    excerpt= article.cssselect(' div.ibm--card__body > p.ibm--card__excerpt')[0].text
    category= article.cssselect('div.ibm--card__bottom > p.cpt-byline__categories span')
    #only two available on block: except '+'

    #announcements.append([link,atype,adate,title,excerpt,[category[0].text,category[1].text]])
    announcements.append([link,atype,adate,title,excerpt,[span.text for span in category if span.text!='+']])

print(announcements)
