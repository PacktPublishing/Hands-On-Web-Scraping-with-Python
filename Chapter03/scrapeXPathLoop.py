import lxml.html
from lxml.etree import XPath

baseUrl = "http://books.toscrape.com/"
bookUrl = "http://books.toscrape.com/catalogue/category/books/food-and-drink_33/index.html"
pageUrl = "http://books.toscrape.com/catalogue/category/books/food-and-drink_33/page-"

dataSet = []
page=1
totalPages=1
while(page<=totalPages):
    print("Rows in Dataset: "+str(len(dataSet)))

    if(page==1):
        doc = lxml.html.parse(pageUrl+str(page)+".html").getroot()
        perPageArticles = doc.xpath("//*[@id=\"default\"]//form/strong[3]/text()")
        totalArticles = doc.xpath("//*[@id=\"default\"]//form/strong[1]/text()")
        totalPages = round(int(totalArticles[0])/int(perPageArticles[0]))
        print(str(totalArticles[0])+" Results, showing "+str(perPageArticles[0])+" Articles per page")
    else:
        doc = lxml.html.parse(pageUrl+str(page)+".html").getroot()

    #used to find page url pattern
    nextPage = doc.xpath("//*[@id=\"default\"]//ul[contains(@class,'pager')]/li[2][contains(@class,'next')]/a/@href")
    if len(nextPage)>0:    
        print("Scraping Page "+str(page)+" of "+str(totalPages)+". NextPage > "+str(nextPage[0]))
    else:
        print("Scraping Page "+str(page)+" of "+str(totalPages))
    
    articles = XPath("//*[@id='default']//ol/li[position()>0]")
    titlePath = XPath(".//article[contains(@class,'product_pod')]/h3/a/text()")
    pricePath = XPath(".//article/div[2]/p[contains(@class,'price_color')]/text()")
    stockPath = XPath(".//article/div[2]/p[2][contains(@class,'availability')]/text()[normalize-space()]")
    imagePath = XPath(".//article/div[1][contains(@class,'image_container')]/a/img/@src")
    starRating = XPath(".//article/p[contains(@class,'star-rating')]/@class")
    
    for row in articles(doc):
        title = titlePath(row)[0]
        price = pricePath(row)[0]
        availability = stockPath(row)[0].strip()
        image = imagePath(row)[0]
        rating = starRating(row)[0]
    
        dataSet.append([title,price,availability,image.replace('../../../..',baseUrl),rating.replace('star-rating ','')])

    page+=1

print(dataSet)
