from webbrowser import Chrome
import pytest
import time
from Test_login import *

@pytest.mark.run(order=7)
class Test_policy(Test_login):

    def test_b_policy(self, test_a_login):
        #hamburger
        self.webdriver.implicitly_wait(50000)
        self.webdriver.find_element_by_xpath("//div[contains(@class,'mdl-layout__drawer-button')]").click()
        #self.webdriver.implicitly_wait(50000)
        time.sleep(5)
        self.webdriver.find_element_by_xpath("//span[contains(text(),'Privacy Policy')]").click()             #policy page
        print("Policy Page")
        time.sleep(7)
        self.webdriver.find_element_by_xpath("//div[contains(@class,'mdl-layout__drawer-button')]").click()
        time.sleep(5)
        self.webdriver.find_element_by_id("menu-top-right").click()
        time.sleep(5)
        self.webdriver.find_element_by_xpath("//body/div[@id='content']/div[1]/div[1]/div[1]/div[3]/nav[1]/div[2]/div[1]/ul[1]/li[2]/a[1]").click()     #logout button
        print("User logged Out")
        time.sleep(5)
        self.webdriver.close()
        self.webdriver.__exit__()
        time.sleep(5)
