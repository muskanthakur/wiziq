from webbrowser import Chrome
import pytest
import time
from Test_login import *

@pytest.mark.run(order=5)
class Test_classes(Test_login):

    #@pytest.fixture()
    def test_b_classlisting(self, test_a_login):
        #hamburger
        self.webdriver.implicitly_wait(50000)
        self.webdriver.find_element_by_xpath("//div[contains(@class,'mdl-layout__drawer-button')]").click()
        self.webdriver.implicitly_wait(50000)
        time.sleep(5)
        self.webdriver.find_element_by_xpath("//span[contains(text(),'Live Classes')]").click()


        #class listing
        time.sleep(2)
        self.webdriver.find_element_by_xpath("//span[contains(text(),'Past')]").click()  # listing in past tab
        self.webdriver.get("https://jacksparow.wiziqxt.com/admin/my-class-detail/2332750-pdf-issue-2/overview?prevPage=my-classes")
        time.sleep(3)
        self.webdriver.find_element_by_xpath("//*[@id='mainMdlContainer']/header/div[2]/div[1]/ul/li[2]/a").click()
        time.sleep(2)
        self.webdriver.find_element_by_xpath("//*[@id='mainMdlContainer']/div[4]/button/span").click()
        time.sleep(2)
        self.webdriver.find_element_by_xpath("//*[@id='mainMdlContainer']/div[4]/ul/li[2]").click()
        self.webdriver.find_element_by_xpath("//*[@id='enrollUser']/div/div/div/div/ul/li[2]/a/span[2]").click()
        self.webdriver.find_element_by_xpath("//*[@id= 'formList']/div/div[7]/div/div/div/div/div[1]/div/div/ul[1]/li[1]/div/label/span[3]").click()
        self.webdriver.find_element_by_xpath("//*[@id= 'formList']/div/div[7]/div/div/div/div/div[1]/div/div/ul[2]/li[1]/div/label/span[3]").click()
        self.webdriver.find_element_by_xpath("//*[@id= 'formList']/div/div[7]/div/div/div/div/div[1]/div/div/ul[3]/li[1]/div/label/span[3]").click()
        self.webdriver.find_element_by_xpath("//*[@id= 'fromListSubmit']/span[2]").click()
        time.sleep(5)
        self.webdriver.refresh()
        time.sleep(5)
        self.webdriver.close()
        self.webdriver.__exit__()