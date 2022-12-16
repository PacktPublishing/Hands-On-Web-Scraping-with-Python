from pyquery import PyQuery as pq
import requests

sourceUrl='https://developer.ibm.com/announcements/'
dataSet = list()

def read_url(url):
    """Read given Url , Returns pyquery object for page content"""
    pageSource = requests.get(url).content
    return pq(pageSource)

def get_details(page):
    """read 'page' url and append list of queried items to dataSet"""
    response = read_url(page)

    articles = response.find('.developer--card > a.developer--card__block_link')
    print("\nTotal articles found :", articles.__len__(), ' in Page: ', page)
    for article in articles.items():
        link = article.attr('href')
        adate = article.find('div.developer--card__bottom > p > span').text()
        article.find('div.developer--card__bottom > p > span').remove()
        atype = article.find('h5').text().strip()
        title = article.find('h3.developer--card__title').text().encode('utf-8')

        if link:
            link = str(link).replace('/announcements/', sourceUrl)
            categories = [a.text for a in read_url(link).find('.bx--accordion__content > a.bx--tag--blue') ]
            dataSet.append([link, atype, adate, title, ",".join(categories)])

if __name__ == '__main__':
    pageUrl = sourceUrl+"category/data-science/?fa=date:DESC&fb="

    pageUrls = [
        sourceUrl+"category/data-science/page/%(page)s?fa=date:DESC&fb=" % {'page': page}
        for page in range(1, 3)]

    print(pageUrls)

    for pages in pageUrls:
        get_details(pages)

    print("\nTotal articles collected: ", len(dataSet))
    print(dataSet)
