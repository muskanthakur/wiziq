from webbrowser import Chrome
import pytest
import time
from Test_login import *

@pytest.mark.run(order=1)
class Test_Content(Test_login):

    def test_b_content(self, test_a_login):
        time.sleep(5)
        self.webdriver.find_element_by_xpath("//div[contains(@class,'mdl-layout__drawer-button')]").click()
        time.sleep(10)
        self.webdriver.find_element_by_xpath("//span[contains(text(),'Library')]").click()
        time.sleep(5)
        self.webdriver.find_element_by_xpath("//body/div[@id='content']/div[1]/div[1]/div[1]/div[4]/button[1]/span[1]").click()
        self.webdriver.find_element_by_xpath("//body/div[@id='content']/div[1]/div[1]/div[1]/div[4]/ul[1]/li[1]").click()
        time.sleep(5)
        self.webdriver.find_element_by_xpath("//div[@class='fsp-modal']").click()
        #self.webdriver.find_element_by_xpath("//div[@class='fsp-modal']").send_key("Downloads\invitation_academy.csv")
        self.webdriver.close()
        self.webdriver.__exit__()
