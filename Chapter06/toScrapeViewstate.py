from pyquery import PyQuery as pq
import requests

mainurl = "http://toscrape.com/"
searchurl = "http://quotes.toscrape.com/search.aspx"
filterurl = "http://quotes.toscrape.com/filter.aspx"
quoteurl = "http://quotes.toscrape.com/"
authorTags = [('Albert Einstein', 'success'), ('Thomas A. Edison', 'inspirational')]

def processRequests(url, params={}, customheaders={}):
    if len(params) > 0:
        response = requests.post(url, data=params, headers=customheaders)
    else:
        response = requests.get(url)
    #headers = response.headers # print(headers)
    #cookies = response.cookies # print(cookies)
    return pq(response.text)

if __name__ == '__main__':
    for authorTag in authorTags:
        authorName,tagName= authorTag

        #Step 1: load searchURL
        searchResponse = processRequests(searchurl)
        author = searchResponse.find('select#author option:contains("' + authorName + '")').attr('value')
        viewstate = searchResponse.find('input#__VIEWSTATE').attr('value')
        tag = searchResponse.find('select#tag option').text()

        print("Author: ", author)
        print("ViewState: ", viewstate)
        print("Tag: ", tag)

        #Step 2: load filterurl with author and default tag
        params = {'author': author, 'tag': tag, '__VIEWSTATE': viewstate}
        customheaders = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Referer': searchurl
        }
        filterResponse = processRequests(filterurl,params,customheaders)
        viewstate = filterResponse.find('input#__VIEWSTATE').attr('value')
        tagSuccess = filterResponse.find('select#tag option:contains("' + tagName + '")').attr('value')
        submitButton = filterResponse.find('input[name="submit_button"]').attr('value')
        print("Author: ", author)
        print("ViewState: ", viewstate)
        print("Tag: ", tagSuccess)
        print("Submit: ", submitButton)

        #Step 3: load filterurl with author and defined tag
        params = {'author': author, 'tag': tagSuccess, 'submit_button': submitButton, '__VIEWSTATE': viewstate}
        # params = {'author': author, 'tag': tagSuccess, 'submit_button': submitButton}#, '__VIEWSTATE': viewstate}  # test
        customheaders = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Referer': filterurl
        }
        finalResponse = processRequests(filterurl,params, customheaders)

        #Step 4: Extract results
        quote = finalResponse.find('div.quote span.content').text()
        quoteAuthor = finalResponse.find('div.quote span.author').text()
        message = finalResponse.find('div.quote span.tag').text()
        print("Quote: ", quote, "\nAuthor: ", quoteAuthor, "\nMessage: ", message)
