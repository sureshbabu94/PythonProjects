import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from datetime import datetime


s = Service('C:/PythonProjects/Drivers/chromedriver.exe')
driver = webdriver.Chrome(service=s)
url = r"https://demo.guru99.com/test/web-table-element.php"
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(10)
cnames=driver.find_elements(By.XPATH, "//*[@id='leftcontainer']/table/tbody/tr/td/a")
num=len(cnames)
print(type(cnames[0]))
print("cnames: "+str(num))
print(cnames)
list=[]
#Print company names from table
for x in range(0,num):
    print(cnames[x].text)
    list.append(cnames[x].text)

assert "HDIL" in list, "HDIL is not available in the list"
    
trow=driver.find_elements(By.XPATH, "//*[@id='leftcontainer']/table/tbody/tr")


driver.quit()


