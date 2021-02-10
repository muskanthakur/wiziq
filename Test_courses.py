from webbrowser import Chrome
import pytest
import time
from Test_login import *

@pytest.mark.run(order=2)
class Test_courses(Test_login):

    @pytest.fixture()
    def test_b_courselisting(self, test_a_login):
        #course listing
        self.webdriver.implicitly_wait(15)
        self.webdriver.find_element_by_xpath("//span[contains(text(),'Past')]").click()     #course listing in past tab
        print("Course listing Complete")
        time.sleep(5)


    def test_c_coursecreation(self,test_b_courselisting):
        #course creation
        time.sleep(5)
        self.webdriver.find_element_by_xpath("//body/div[@id='content']/div/div/div[@id='mainMdlContainer']/div/button/span[1]").click()
        time.sleep(5)
        self.webdriver.find_element_by_link_text("school").click()
        self.webdriver.implicitly_wait(1000)
        self.frame1 = self.webdriver.find_element_by_id("creationOverlay")
        self.webdriver.switch_to.frame(self.frame1)
        self.webdriver.implicitly_wait(1000)
        self.webdriver.find_element_by_id("lbtnSaveSettings").click()

        # Course schedule
        self.webdriver.find_element_by_id("txtTitle").send_keys("Course created by automation")
        self.webdriver.implicitly_wait(1000)
        self.webdriver.find_element_by_id("lbtnNextProfile").click()

        # course profile
        self.webdriver.find_element_by_id("txtSubTitle").click()
        self.webdriver.find_element_by_id("txtSubTitle").send_keys("This is automated course")
        self.webdriver.find_element_by_id("txtHighlight1").click()
        self.webdriver.find_element_by_id("txtHighlight1").send_keys("First")
        self.webdriver.find_element_by_id("txtHighlight2").click()
        self.webdriver.find_element_by_id("txtHighlight2").send_keys("Second")
        self.webdriver.find_element_by_id("txtHighlight3").click()
        self.webdriver.find_element_by_id("txtHighlight3").send_keys("Third")

        self.frame2 = self.webdriver.find_element_by_id("txtAbtCourse_ifr")
        self.webdriver.switch_to.frame(self.frame2)
        self.webdriver.find_element_by_id("tinymce").click()
        self.webdriver.find_element_by_id("tinymce").send_keys("This is about course")
        self.webdriver.switch_to.parent_frame()
        self.webdriver.find_element_by_xpath("//a[@id='lbtnNextInvite']/span").click()

        #cross button
        time.sleep(5)
        self.webdriver.switch_to.parent_frame()
        time.sleep(10)
        self.webdriver.find_element_by_xpath("//button[contains(@class,'fluidModalClose')]").click()
        self.webdriver.switch_to.default_content()
        self.webdriver.refresh()
        time.sleep(10)
        print("Course Creation Complete")
        self.webdriver.close()
        self.webdriver.__exit__()

