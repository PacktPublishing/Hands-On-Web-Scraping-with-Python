from pyquery import PyQuery as pq
import requests
mainUrl = "http://testing-ground.scraping.pro"
loginUrl = "http://testing-ground.scraping.pro/login"
postUrl="http://testing-ground.scraping.pro/login?mode=login"
logoutUrl = "http://testing-ground.scraping.pro/login?mode=logout"

def responseCookies(response):
    headers = response.headers
    cookies = response.cookies
    print("Headers: ", headers)
    print("Cookies: ", cookies)

def processParams(params):
    response = requests.post(postUrl, data=params)
    responseB = pq(response.text)
    message = responseB.find('div#case_login h3').text()
    print("Confirm Login : ",message)

if __name__ == '__main__':
    requests.get(logoutUrl)
    response = requests.get(mainUrl)
    responseCookies(response)

    response = requests.get(loginUrl)
    responseCookies(response)

    responseA = pq(response.text)
    username = responseA.find('input[id="usr"]').attr('name')
    password = responseA.find('input[id="pwd"]').attr('name')

    #Welcome : Success
    paramsCorrect = {username: 'admin', password: '12345'} #Success
    print(paramsCorrect)
    processParams(paramsCorrect)

    paramsIncorrect = {username: 'admin', password: '123456'} #Access Denied
    print(paramsIncorrect)
    processParams(paramsIncorrect)
