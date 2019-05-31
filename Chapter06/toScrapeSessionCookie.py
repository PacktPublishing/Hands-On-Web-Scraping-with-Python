from pyquery import PyQuery as pq
import requests
mainUrl = "http://toscrape.com/"
loginUrl = "http://quotes.toscrape.com/login"
quoteUrl = "http://quotes.toscrape.com/"

def getCustomHeaders(cookieHeader):
    return {
        'Host': 'quotes.toscrape.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Referer': 'http://quotes.toscrape.com/login',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': cookieHeader,
    }

def responseCookies(response):
    headers = response.headers
    cookies = response.cookies
    print("Headers: ", headers)
    print("Cookies: ", cookies)
    return headers['Set-Cookie']

if __name__ == '__main__':
    requests.get(mainUrl)
    response = requests.get(loginUrl)
    setCookie = responseCookies(response)
    print("Set-Cookie: ",setCookie)

    responseA = pq(response.text)
    csrf_token = responseA.find('input[name="csrf_token"]').attr('value')
    username = responseA.find('input[id="username"]').attr('name')
    password = responseA.find('input[id="password"]').attr('name')
    params = {username: 'test', password: 'test','csrf_token': csrf_token}
    print(params)

    customheaders = getCustomHeaders(setCookie)
    response = requests.post(loginUrl, data=params, headers=customheaders)
    # response = requests.post(loginUrl, data=params, headers={})
    setCookie = responseCookies(response)
    #print("Set-Cookie: ",setCookie)

    responseB = pq(response.text)
    logoutText = responseB.find('a[href*="logout"]').text()
    logoutLink = responseB.find('a[href*="logout"]').attr('href')
    print("Current Page : ",response.url)
    print("Confirm Login : ", responseB.find('.row h2').text())
    print("Logout Info : ", logoutText," & ",logoutLink)
