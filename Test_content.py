from webbrowser import Chrome

import pytest
import time


# noinspection PyGlobalUndefined
class Test_content():
    from selenium import webdriver
    global webdriver
    webdriver.Chrome("C:\\Users\\asus\\PycharmProjects\\Wiziqxt\\drivers\\chromedriver.exe")

    @pytest.fixture()
    def test_a_login(self):
        self.webdriver = webdriver.Chrome("C:\\Users\\asus\\PycharmProjects\\Wiziqxt\\drivers\\chromedriver.exe")
        self.webdriver.get("http://admin2016.ng.qe.wiziqinternal.com/authentication/login")
        self.webdriver.maximize_window()
        #login
        self.webdriver.find_element_by_id("email").click()
        self.webdriver.find_element_by_id("email").send_keys("adminqa@yopmail.com")
        self.webdriver.find_element_by_id("password").click()
        self.webdriver.find_element_by_id("password").send_keys("111111111111111")
        self.webdriver.find_element_by_class_name("mdl-button__ripple-container").click()
        print("Login Is Complete")



    def test_b_content(self, test_a_login):
        #hamburger
        time.sleep(5)
        self.webdriver.find_element_by_xpath("//div[contains(@class,'mdl-layout__drawer-button')]").click()
        time.sleep(5)
        self.webdriver.find_element_by_xpath("//span[contains(text(),'Library')]").click()
        time.sleep(5)
        self.webdriver.find_element_by_xpath("//body/div[@id='content']/div[1]/div[1]/div[1]/div[4]/button[1]/span[1]").click()
        self.webdriver.find_element_by_xpath("//body/div[@id='content']/div[1]/div[1]/div[1]/div[4]/ul[1]/li[1]").click()
        time.sleep(5)
        self.webdriver.find_element_by_xpath("//div[@class='fsp-modal']").click()
        self.webdriver.find_element_by_xpath("//div[@class='fsp-modal']").send_key("Downloads\invitation_academy.csv")

