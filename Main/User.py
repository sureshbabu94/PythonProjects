import json
import requests, time
o=time.time()
x=requests.get('https://jsonplaceholder.typicode.com/users')
c=time.time()
print("EXEC TIME: ",c-o)
#Status Code 200
print(x.status_code)
#Status Message OK
print(x.reason)
#Request Method GET
print(x.request.method)
#Response Time
print(x.elapsed)
#Response Content
print(x.content)
#Request Headers
print(x.request.headers)
#List of Response Headers
print(x.headers)
#Get Response Header
print(x.headers['Content-Type'])
#JSON Response
print(x.json())
#Cookies List of Tuples
print(x.cookies.items())



'''
session = requests.Session()
response = session.get('http://google.com')
print(session.cookies.get_dict())
'''
