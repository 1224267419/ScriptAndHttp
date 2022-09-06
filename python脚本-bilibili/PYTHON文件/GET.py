import requests

url0= "https://www.baidu.com"
r0=requests.get(url0)
print(r0.url)
print(r0)
print(r0.text)