from datetime import datetime
import allure
import pytest

import test_flip
from allure_commons.types import AttachmentType


def step(fun):
    def inner():
        fun()
        #allure.attach(self.driver.get_screenshot_as_png(), fun.__name__, allure.attachment_type.PNG)
        print("step")

    return inner

@pytest.fixture()
def drive():
    print("drive")


@pytest.mark.usefixtures("drive")
@step
def test_page():
    print("page")




'''
def decofun(fun):
    def subfun():
        fun()
        t = datetime.now()
        print("t:" + str(t))
        p = t.strftime("%d-%m-%Y-%H-%M-%S-%f")
        self.driver.save_screenshot("C:/PythonProjects/scr/flipkarthome-" + p + ".png")
        print("Took Screenshots..........")
    return subfun

@decofun
def furios():
    print("fun")

'''