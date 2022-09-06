import requests

url = "http://127.0.0.1/brute/brute_post.pl"
data ={'username':'admin',
       'password':'admin',
       'submit':'登录'}
r=requests.post(url,data=data)
print(r.status_code)    #状态码
if r.text.find('succ'):
    print('admin : admin' + 'successful')