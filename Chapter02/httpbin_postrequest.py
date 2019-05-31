import requests
params = {'custname':'Mr. ABC','custtel':'','custemail':'abc@somedomain.com',
'size':'small','topping':['cheese','mushroom'],'delivery':'13:00','comments':'None'}
headers={
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Content-Type':'application/x-www-form-urlencoded',
    'Referer':'http://httpbin.org/forms/post'
    }
response = requests.post('http://httpbin.org/post',data=params,headers=headers).json()
print(response)