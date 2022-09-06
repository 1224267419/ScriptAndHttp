import  requests

url0 ='http://10.0.3.2:801/eportal/portal/login'
payload ={'callback':'dr1003','login_method':1,'user_account':' 0 3120007371','user_password':'Lyb23366','lang':'zh-cn','v':'4574','lang':'zh'}
headers={'User-Agent':'HAHA'}
r=requests.get(url0,payload,headers=headers)
r1=requests.get(url0,payload)
print(r.request.headers)
print(r1.request.headers)

print(r.text)
