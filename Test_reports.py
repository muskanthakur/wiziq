from webbrowser import Chrome
import pytest
import time
from Test_login import *

@pytest.mark.run(order=7)
class Test_reports(Test_login):

    def test_b_reportslist(self, test_a_login):
        #hamburger
        self.webdriver.implicitly_wait(50000)
        self.webdriver.find_element_by_xpath("//div[contains(@class,'mdl-layout__drawer-button')]").click()
        #self.webdriver.implicitly_wait(50000)
        time.sleep(5)
        self.webdriver.find_element_by_xpath("//span[contains(text(),'Reports')]").click()             #courses report
        print("Report Of Courses")

        #reports
        time.sleep(5)
        self.webdriver.find_element_by_xpath("//header/div[2]/div[1]/ul[1]/li[2]/a[1]").click()        #classes report
        print("Report Of Classes")
        time.sleep(5)
        self.webdriver.find_element_by_xpath("//header/div[2]/div[1]/ul[1]/li[3]/a[1]").click()        #learner report
        print("Report Of Learners")
        self.webdriver.close()
        self.webdriver.__exit__()
