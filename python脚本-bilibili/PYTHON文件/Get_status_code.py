import  requests

url0 ='http://10.0.3.2:801/eportal/portal/login'
payload ={'callback':'dr1003','login_method':1,'user_account':' 0 3120007371','user_password':'Lyb23366','lang':'zh-cn','v':'4574','lang':'zh'}
r=requests.get(url0,payload)
print(r)
print(r.text)#输出成功
print(r.content)
if str(r.content).find('succ'):#转化为字符串
    print('successful')