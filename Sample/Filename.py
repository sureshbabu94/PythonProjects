import os,openpyxl
book = openpyxl.Workbook()
sheet = book.active
l=os.listdir('C:/Users/10872/testa/testa-catalog/catalog/rocky/salesforce/TM_Lead/qafull')

n=len(l)
for x in range(1,n+1):
    s=l[x-1].split(".py")
    print(s[0])
    sheet.cell(row=x, column=1).value = s[0]

book.save('C:/Users/10872/Documents/ShareX/book.xlsx')
book.close()
