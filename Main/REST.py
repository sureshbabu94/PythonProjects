import requests
s=requests.session()
s.get("https://www.google.com/search?q=hello")
print(s.cookies)
print(s.cookies['AEC'])
s.cookies['AAC']='SKC'
s.get("https://www.google.com/search?q=HI")
print(s.cookies)
print(s.cookies['AEC'])
print(s.cookies['AAC'])
s.get("https://www.bing.com/search?q=hello")
print("BING bing",s.cookies)
print(s.cookies['AEC'])
print(s.cookies['AAC'])
r=requests.get("https://www.google.com/search?q=hello")
print("R1",r.cookies)
print("R1",r.cookies['AEC'])
r.cookies['AAC']='SKC'
r2=requests.get("https://www.google.com/search?q=hi")
print("Google R2",r2.cookies)
print("R2 AEC",r2.cookies['AEC'])
print("R2 AAC",r2.cookies['AAC'])
try:
    requests.sample
except NameError:
    pass

