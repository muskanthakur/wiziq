from webbrowser import Chrome
import pytest
import time


class Test_login():
    from selenium import webdriver
    global webdriver
    webdriver.Chrome("C:\\Users\\asus\\PycharmProjects\\Wiziqxt\\drivers\\chromedriver.exe")

    @pytest.fixture()
    def test_a_login(self):
        self.webdriver = webdriver.Chrome("C:\\Users\\asus\\PycharmProjects\\Wiziqxt\\drivers\\chromedriver.exe")
        self.webdriver.get("https://jacksparow.wiziqxt.com/authentication/login")
        self.webdriver.maximize_window()
        #login
        self.webdriver.find_element_by_id("email").click()
        self.webdriver.find_element_by_id("email").send_keys("jack@yopmail.com")
        self.webdriver.find_element_by_id("password").click()
        self.webdriver.find_element_by_id("password").send_keys("123456")
        self.webdriver.find_element_by_class_name("mdl-button__ripple-container").click()
        print("Login Is Complete")