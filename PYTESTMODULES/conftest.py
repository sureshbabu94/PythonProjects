from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pytest, logging,os,allure
from datetime import datetime
from selenium.webdriver.common.by import By
from Reader import WebReader
from xml.dom import minidom
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture()
def browser(request):
    file = minidom.parse("C:\\PythonProjects\\webelements\\config.xml")
    print(file.nodeName)
    print(file.firstChild.tagName)
    tag = file.getElementsByTagName('subchild1')
    btype=tag[0].firstChild.nodeValue

    s = Service('./Drivers/chromedriver.exe')
    dr_driver=None
    if btype=="chrome":
        #driver = webdriver.Chrome(service=s)
        dr_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    if btype=="firefox":
        #driver = webdriver.Firefox(executable_path='./Drivers/geckodriver.exe')
        dr_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    dr_driver.delete_all_cookies()
    dr_driver.get(WebReader.geturl())
    dr_driver.maximize_window()
    dr_driver.implicitly_wait(WebReader.getimplicitwait())
    logging.warning("Browser Opened")
    dr_driver.find_element(By.XPATH, WebReader.getlocator("closeBtn")).click()
    request.cls.driver=dr_driver
    yield
    dr_driver.quit()

