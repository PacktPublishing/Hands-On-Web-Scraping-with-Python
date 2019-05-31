'''
Listing Quotes from first 5 or less pages found
from 'http://quotes.toscrape.com/'
'''

import requests
import re
from bs4 import BeautifulSoup
import csv

sourceUrl = 'http://quotes.toscrape.com/'
keys = ['quote_tags','author_url','author_name','born_date','born_location','quote_title']


def read_url(url):
    """Read given Url , Returns requests object for page content"""
    response = requests.get(url)
    return response.text


def get_details(page, dataWriter):
    """Get 'response' for first 5 pages, parse it and collect data for 'keys' headers"""
    nextPage = True
    pageNo = 1
    while (nextPage and pageNo <= 5):
        response = read_url(page + 'page/' + str(pageNo))
        soup = BeautifulSoup(response, 'lxml')

        rows = soup.find_all('div', 'quote')
        if (len(rows) > 0):
            print("Page ",pageNo," Total Quotes Found ",len(rows))
            for row in rows:
                if row.find('span',attrs={'itemprop':'text'}):

                    title = row.find(attrs={'itemprop':'text'}).text.strip()
                    author = row.find(attrs={'itemprop':'author'}).text.strip()
                    authorLink = row.find('a',href=re.compile(r'/author/')).get('href')
                    tags = row.find('div','tags').find(itemprop="keywords").get('content')
                    print(title, ' : ', author,' : ',authorLink, ' : ',tags)

                    if authorLink:
                        authorLink = 'http://quotes.toscrape.com' + authorLink
                        linkDetail = read_url(authorLink)
                        soupInner = BeautifulSoup(linkDetail, 'lxml')

                        born_date = soupInner.find('span','author-born-date').text.strip()
                        born_location = soupInner.find('span','author-born-location').text.strip()

                        # Write a list of values in file
                        dataWriter.writerow([tags,authorLink,author,born_date,born_location.replace('in ',''),title])

            nextPage = True
            pageNo += 1
        else:
            print("Quotes Not Listed!")



if __name__ == '__main__':
    dataSet = open('quotes.csv', 'w', newline='', encoding='utf-8')
    dataWriter = csv.writer(dataSet)
    # Write a Header or Column_names to CSV
    dataWriter.writerow(keys)
    get_details(sourceUrl, dataWriter)
    # get_details(sourceUrl)
    dataSet.close()
