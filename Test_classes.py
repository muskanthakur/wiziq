from webbrowser import Chrome
import pytest
import time
from Test_login import *

@pytest.mark.run(order=3)
class Test_classes(Test_login):

    @pytest.fixture()
    def test_b_classlisting(self, test_a_login):
        #hamburger
        self.webdriver.implicitly_wait(50000)
        self.webdriver.find_element_by_xpath("//div[contains(@class,'mdl-layout__drawer-button')]").click()
        self.webdriver.implicitly_wait(50000)
        time.sleep(5)
        self.webdriver.find_element_by_xpath("//span[contains(text(),'Live Classes')]").click()


        #class listing
        time.sleep(10)
        self.webdriver.implicitly_wait(5000)
        self.webdriver.find_element_by_xpath("//span[contains(text(),'Past')]").click()  # listing in past tab
        print("Class Listing Complete")


    def test_c_classcreation(self,test_b_classlisting ):
        #class creation
        time.sleep(5)
        self.webdriver.find_element_by_xpath("//div[@id='mainMdlContainer']/div[4]/div/span").click()
        self.webdriver.implicitly_wait(1000)
        self.frame3 = self.webdriver.find_element_by_id("creationOverlay")
        self.webdriver.switch_to_frame(self.frame3)
        self.webdriver.find_element_by_id("txtTitle").click()
        self.webdriver.find_element_by_id("txtTitle").send_keys("Automated class")
        self.webdriver.find_element_by_id("txtTagline").click()
        self.webdriver.find_element_by_id("txtTagline").send_keys("This is to automate class")
        self.webdriver.find_element_by_class_name("ulink").click()
        self.webdriver.find_element_by_id("txtDescription").click()
        self.webdriver.find_element_by_id("txtDescription").send_keys("This is automated class")
        self.webdriver.find_element_by_id("rdpublic").click()
        self.webdriver.find_element_by_id("rdoFree").click()
        self.webdriver.find_element_by_id("rdbNoSignUpYes").click()
        self.webdriver.find_element_by_id("btnSchedule").click()

        # cross button
        time.sleep(5)
        self.webdriver.switch_to.parent_frame()
        time.sleep(10)
        self.webdriver.find_element_by_xpath("//button[contains(@class,'fluidModalClose')]").click()
        self.webdriver.switch_to.default_content()
        self.webdriver.refresh()
        time.sleep(10)
        print("Class Creation Complete")
        self.webdriver.close()
        self.webdriver.__exit__()



