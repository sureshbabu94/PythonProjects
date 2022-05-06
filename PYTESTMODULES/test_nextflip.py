import time, unittest, sys, logging, pytest, traceback,allure, openpyxl,re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from datetime import datetime
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import ElementClickInterceptedException, ElementNotInteractableException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Reader import ExcelReader
from Reader import WebReader
from Base import Invoke
from PYTESTMODULES.base_test import BasicTest



def get_data(filepath):
    workbook = openpyxl.load_workbook(filepath)
    sheet = workbook.active
    totalrows = sheet.max_row
    totalcols = sheet.max_column
    datalist = []
    for i in range(1, totalrows + 1):
        record = []
        for j in range(1, totalcols + 1):
            celldata = sheet.cell(row=i, column=j).value
            record.insert(j, celldata)
        t = tuple(record)
        datalist.insert(i, t)
    return datalist

class TestMain(BasicTest):

    def screencaptured(fun):
        def inner(self):
            fun(self)
            allure.attach(self.driver.get_screenshot_as_png(), fun.__name__, allure.attachment_type.PNG)
            print("Allure Takes screenshot")

        return inner
    def screencaptureparam(fun):
        def inner(self,product):
            fun(self,product)
            allure.attach(self.driver.get_screenshot_as_png(), fun.__name__, allure.attachment_type.PNG)
            print("Allure Takes screenshot")

        return inner


    @screencaptured
    def test_click_close(self):
        self.driver.find_element(By.XPATH, WebReader.getlocator("searchbar")).send_keys(ExcelReader.product1)
        act = ActionChains(self.driver)
        srchele = self.driver.find_element(By.XPATH, WebReader.getlocator("searchicon"))
        act.move_to_element(srchele).click().perform()
        logging.info("Product searched........")
        min = Select(self.driver.find_element(By.XPATH, WebReader.getlocator("minimum")))
        min.select_by_value("50000")
        max = Select(self.driver.find_element(By.XPATH, WebReader.getlocator("maximum")))
        max.select_by_value("Max")
        logging.info("Pricefilter............")
        # self.browser.execute_script('arguments[0].click', Base.fassured)
        wait = WebDriverWait(self.driver, 10)
        # wait.until(EC.element_to_be_clickable((By.XPATH,Base.fassure)))
        self.driver.execute_script('arguments[0].click', WebReader.getlocator("fassure"))
        #self.driver.find_element(By.XPATH, WebReader.getlocator("fassure")).click()
        time.sleep(3)
        logging.info("Fassured..............")
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, WebReader.getlocator("prod1"))))
        try:
            time.sleep(5)
            self.driver.find_element(By.XPATH, WebReader.getlocator("prod1")).click()
        except ElementClickInterceptedException:
            logging.info("Click exception occured...")
        except:
            logging.info("Unknown exception occured...")
            traceback.print_exc()
        logging.info("clicked for window")
        parent = self.driver.current_window_handle
        logging.info("Parent " + parent)
        child = self.driver.window_handles
        logging.info(child)
        self.driver.switch_to.window(child[1])
        logging.info("switched window..............")
        #self.driver.execute_script('arguments[0].scrollIntoView', WebReader.getlocator("interest"))
        self.driver.find_element(By.XPATH, WebReader.getlocator("addtocart")).click()
        self.driver.find_element(By.XPATH, WebReader.getlocator("placeorder")).click()
        print("add to cart..............")
    def close_icon(self):
        self.driver.find_element(By.XPATH, WebReader.getlocator("closeBtn")).click()


    @pytest.mark.parametrize("product", get_data("C:\\PythonProjects\\webelements\\products.xlsx"))
    @screencaptureparam
    def test_multipleproduct(self,product):
        self.driver.find_element(By.XPATH, WebReader.getlocator("searchbar")).clear()
        self.driver.find_element(By.XPATH, WebReader.getlocator("searchbar")).send_keys(product)
        allure.attach(self.driver.get_screenshot_as_png(), "product", allure.attachment_type.PNG)





