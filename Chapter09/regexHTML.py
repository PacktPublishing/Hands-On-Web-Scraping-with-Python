'''
In this code we will be using Regex to find the listed information from the HTML content:
-HTML elements,
-Elements attributes ('key' and 'values') and
-Elements content.
'''

import re
from bs4 import BeautifulSoup


def read_file():
    '''
    Read and return content from file (.html).
    '''
    content = open("regexHTML.html", "r")
    pageSource = content.read()
    return pageSource


def applyPattern(pattern):
    tags = re.findall(pattern, page)
    print("Pattern r'{}' ,Found total: {}".format(pattern, len(tags)))
    print(tags)
    return


if __name__ == "__main__":
    page = read_file()  # .decode('utf-8')
    soup = BeautifulSoup(page, 'lxml')
    print([tag.name for tag in soup.find_all()])
    # ['html', 'head', 'title', 'style', 'body', 'h1', 'a', 'a', 'a', 'div', 'p', 'i', 'img', 'p', 'i', 'h1']

    applyPattern(r'<(\w+)>')  # Finding Elements without attributes
# Pattern r'<(\w+)>' ,Found total: 6
# ['html', 'head', 'title', 'body', 'div', 'i']

    applyPattern(r'<(\w+)\s')  # Finding Elements with attributes
# Pattern r'<(\w+)\s' ,Found total: 10
# ['style', 'h1', 'a', 'a', 'a', 'p', 'img', 'p', 'i', 'h1']

    applyPattern(r'<(\w+)\s?')  # Finding all HTML element
# Pattern r'<(\w+)\s?' ,Found total: 16
# ['html', 'head', 'title', 'style', 'body', 'h1', 'a', 'a', 'a', 'div', 'p', 'i', 'img', 'p', 'i', 'h1']

    applyPattern(r'<\w+\s+(.*?)=')  # Finding attributes name
# Pattern r'<\w+\s+(.*?)=' ,Found total: 10
# ['type', 'style', 'href', 'class', 'id', 'id', 'src', 'class', 'style', 'itemprop']

    applyPattern(r'(\w+)=')  # Finding names of all attributes
# Pattern r'(\w+)=' ,Found total: 18
# ['type', 'style', 'href', 'style', 'class', 'href', 'id', 'href', 'style', 'id', 'class', 'src', 'id', 'class', 'class', 'id', 'style', 'itemprop']

    applyPattern(r'=\"(\w+)\"')
# Pattern r'=\"(\w+)\"' ,Found total: 9
# ['classOne', 'idOne', 'mainContent', 'content', 'pageLogo', 'logo', 'content', 'subContent', 'subheading']

    applyPattern(r'=\"([\w\S]+)\"')
# Pattern r'=\"([\w\S]+)\"' ,Found total: 18
# ['text/css', 'color:orange;', 'https://www.google.com', 'color:red;', 'classOne', 'https://www.yahoo.com', 'idOne', 'https://www.wikipedia.org', 'color:blue;', 'mainContent', 'content', 'mylogo.png', 'pageLogo', 'logo', 'content', 'subContent', 'color:red', 'subheading']

    applyPattern(r'\>(.*)\<')
# Pattern r'\>(.*)\<' ,Found total: 8
# ['Welcome to Web Scraping: Example', 'Welcome to Web Scraping', 'Google', 'Yahoo', 'Wikipedia', 'Paragraph contents', 'Sub paragraph content', 'Sub heading Content!']
