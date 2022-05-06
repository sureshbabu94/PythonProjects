import requests, json, sys
from requests.auth import *
uid={"username" : "admin", "password" : "password123"}
res=requests.post("https://restful-booker.herokuapp.com/auth",data=uid)
out=res.json()
token=out['token']
print(token)

data2={
    "firstname" : "Sim",
    "lastname" : "Brown",
    "totalprice" : 111,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
}


#ses2=requests.Session.post(self="",url="https://restful-booker.herokuapp.com/booking",data=data2,headers={'Authorization': token})
res2=requests.post("https://restful-booker.herokuapp.com/booking",json=data2)
out2=res2.json()
print(res.status_code,res2.reason)
print(out2['bookingid'])
putid=out2['bookingid']
putdata3={
    "firstname" : "PUT",
    "lastname" : "PUT",
    "totalprice" : 111,
    "depositpaid" :True,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
}
res3=requests.put("https://restful-booker.herokuapp.com/booking/{}".format(putid),json=putdata3,auth=('admin','password123'))
print(res3.status_code,res3.reason)
out3=res3.json()
print(out3)
patchdata4={
    "firstname" : "PATCH",
    "lastname" : "PATCH"
}
res4=requests.patch("https://restful-booker.herokuapp.com/booking/{}".format(putid),json=patchdata4,auth=('admin','password123'))
print(res4.status_code,res4.reason)
out4=res4.json()
print(out4)
delid=out2['bookingid']
res5=requests.delete("https://restful-booker.herokuapp.com/booking/{}".format(delid),auth=('admin','password123'))
print(res5.status_code,res5.reason)
