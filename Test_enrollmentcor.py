import selenium
from selenium import webdriver
import webbrowser
import pytest
import time
from Test_login import *

@pytest.mark.run(order=4)
class Test_enrollmentcor(Test_login):

    #@pytest.fixture()
    def test_b_courselist(self, test_a_login):
        time.sleep(5)
        self.webdriver.get("https://jacksparow.wiziqxt.com/admin/course/117744-course-created-by-automation/overview?prevPage=my-courses")
        self.webdriver.find_element_by_xpath("//header/div[2]/div[1]/ul[1]/li[3]/a[1]").click()
        time.sleep(2)
        self.webdriver.find_element_by_xpath("//*[@id='mainMdlContainer']/div[4]/button/span").click()
        time.sleep(2)
        self.webdriver.find_element_by_xpath("//*[@id='mainMdlContainer']/div[4]/ul/li[2]").click()
        time.sleep(2)
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









