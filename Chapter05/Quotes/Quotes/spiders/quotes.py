# -*- coding: utf-8 -*-
import scrapy
from Quotes.items import QuotesItem

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["quotes.toscrape.com"]

    #To be used for pagination purpose.

    start_urls = (
        'http://quotes.toscrape.com/',
    )
    '''
    #or
    start_urls = (
        'http://quotes.toscrape.com/',
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    )
    or
    start_urls = ['http://quotes.toscrape.com/page/%s' % page for page in xrange(1, 5)]
    '''

    '''Using XPath'''
    def parse(self, response):
        print("Response Type >>> ", type(response))
        rows = response.xpath("//div[@class='quote']")
        
        print("Quotes Count >> ", rows.__len__())
        for row in rows:
            item = QuotesItem()
			
            item['tags'] = row.xpath('div[@class="tags"]/meta[@itemprop="keywords"]/@content').extract_first()
            item['author'] = row.xpath('//span/small[@itemprop="author"]/text()').extract_first()
            item['quote'] = row.xpath('span[@itemprop="text"]/text()').extract_first()
            item['author_link'] = row.xpath('//a[contains(@href,"/author/")]/@href').extract_first()
            if len(item['author_link'])>0:
                item['author_link'] = 'http://quotes.toscrape.com'+item['author_link']

            yield item

        nextPage = response.xpath("//ul[@class='pager']//li[@class='next']/a/@href").extract_first()
        if nextPage:
            print("Next Page URL: ",nextPage)
            #nextPage obtained from either XPath or CSS can be used.
            yield scrapy.Request('http://quotes.toscrape.com'+nextPage,callback=self.parse)

        print('Completed')

   


    '''Using CSS Selectors'''
    '''
    def parse(self, response):
        print("Response Type >>> ", type(response))
        rows = response.css("div.quote")

        for row in rows:
            item = QuotesItem()
            item['tags'] = row.css('div.tags > meta[itemprop="keywords"]::attr("content")').extract_first()
            item['author'] = row.css('small[itemprop="author"]::text').extract_first()
            item['quote'] = row.css('span[itemprop="text"]::text').extract_first()
            item['author_link'] = row.css('a:contains("(about)")::attr(href)').extract_first()
            if len(item['author_link'])>0:
                item['author_link'] = 'http://quotes.toscrape.com'+item['author_link']

            yield item

        nextPage = response.css("ul.pager > li.next > a::attr(href)").extract_first()
        if nextPage:
            print("Next Page URL: ",nextPage)
            #nextPage obtained from either XPath or CSS can be used.
            yield scrapy.Request('http://quotes.toscrape.com'+nextPage,callback=self.parse)

        print('Completed')
        '''
