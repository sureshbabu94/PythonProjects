import requests, json, openpyxl,os
url="https://postman-echo.com/post"
myparams = {'name': 'ABC', 'email':'xyz@gmail.com'}
res = requests.post(url, data=myparams)
t=res.text
print(type(t),t)
s=res.json()
print(type(s),s)
f=s['form']
print(f)
for i,j in f.items():


    if "@gmail.com" in j:
        print("True")

res1=requests.get("https://restful-booker.herokuapp.com/booking/1")
test=res1.json()
print(type(test))
wb = openpyxl.load_workbook('C:\\PythonProjects\\webelements\\testdata.xlsx')
sheet=wb.active
rownum =sheet.max_row
colnum=sheet.max_column
c={}
print(rownum,colnum)
for i in range(1,2):

    for j in range(1, colnum + 1):
        celldata = sheet.cell(row=i, column=j).value
        c[celldata]=""
print(c)

for e,k in enumerate(c,1):

    print(e,k)
    celldata=sheet.cell(row=2,column=e).value
    c[k]=celldata
wb.close()
print(c['Col1'])

list=[{1:1,2:2,3:3},{"a":"a","b":"b","c":"c"}]
d={}
for x in list:
    for y,z in x.items():
        d[y]=z

print(d)
print(os.path)

