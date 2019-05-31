from pyquery import PyQuery as pq

sourceUrl = 'http://quotes.toscrape.com/tag/books/'
dataSet = list()
keys = ['quote_tags','author_url','author_name','born_date','born_location','quote_title']

def read_url(url):
    """Read given Url , Returns pyquery object for page content"""
    pageSource = pq(url)
    return pq(pageSource)


def get_details(page):
    """read 'page' url and append list of queried items to dataSet"""
    nextPage = True
    pageNo = 1
    while (nextPage):
        response = read_url(page + 'page/' + str(pageNo))
        if response.find("ul.pager:has('li.next')"):
            nextPage = True
        else:
            nextPage = False

        quotes = response.find('.quote')
        print("\nTotal Quotes found :", quotes.__len__(), ' in Page: ', pageNo)
        for quote in quotes.items():
            title = quote.find('[itemprop="text"]:first').text()
            author = quote.find('[itemprop="author"]:first').text()
            authorLink = quote.find('a[href*="/author/"]:first').attr('href')
            tags = quote.find('.tags [itemprop="keywords"]').attr('content')

            if authorLink:
                authorLink = 'http://quotes.toscrape.com' + authorLink
                linkDetail = read_url(authorLink)
                born_date = linkDetail.find('.author-born-date').text()
                born_location = linkDetail.find('.author-born-location').text()
                if born_location.startswith('in'):
                    born_location = born_location.replace('in ','')
                dataSet.append(dict(zip(keys,[tags,authorLink,author,born_date,born_location,title[0:50]])))
        pageNo += 1

if __name__ == '__main__':
    get_details(sourceUrl)
    print("\nTotal Quotes collected: ", len(dataSet))
    print(dataSet)
    for info in dataSet:
        print(info['author_name'],' born on ',info['born_date'], ' in ',info['born_location'])

