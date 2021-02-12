from webbrowser import Chrome
import pytest
import time
from Test_login import *

@pytest.mark.run(order=6)
class Test_academysettings(Test_login):

    @pytest.fixture()
    def test_b_settings(self, test_a_login):
        #hamburger
        self.webdriver.implicitly_wait(50000)
        self.webdriver.find_element_by_xpath("//div[contains(@class,'mdl-layout__drawer-button')]").click()
        self.webdriver.implicitly_wait(50000)
        time.sleep(5)
        self.webdriver.find_element_by_xpath("//span[contains(text(),'Academy Settings')]").click()

        #General settings
        time.sleep(5)
        self.webdriver.find_element_by_xpath("//body/div[@id='content']/div[1]/div[1]/div[1]/main[1]/div[1]/div[1]/section[2]/div[1]/div[1]/div[1]/div[1]/div[1]/figure[1]/a[1]/span[1]/em[1]").click()
        time.sleep(5)
        self.webdriver.find_element_by_xpath(" //body/div[@id='content']/div[1]/div[1]/div[1]/main[1]/div[1]/div[1]/section[1]/div[1]/ul[1]/li[1]/a[1]/span[1]").click()
        print("General Settings Page")


    @pytest.fixture()
    def test_c_management(self, test_b_settings):         #user-management
        time.sleep(5)
        self.webdriver.find_element_by_xpath("//body/div[@id='content']/div[1]/div[1]/div[1]/main[1]/div[1]/div[1]/section[2]/div[1]/div[1]/div[2]/div[1]/div[1]/figure[1]/a[1]/span[1]/em[1]").click()
        time.sleep(5)
        self.webdriver.find_element_by_xpath("//body/div[@id='content']/div[1]/div[1]/div[1]/main[1]/div[1]/div[1]/section[1]/div[1]/ul[1]/li[1]/a[1]/span[1]").click()
        print("User Management Page")


    @pytest.fixture()
    def test_d_roles(self, test_c_management):             #roles
        time.sleep(5)
        self.webdriver.find_element_by_xpath("//em[contains(text(),'person_add')]").click()
        time.sleep(5)
        self.webdriver.find_element_by_xpath("//body/div[@id='content']/div[1]/div[1]/div[1]/main[1]/div[1]/div[1]/section[1]/div[1]/ul[1]/li[1]/a[1]/span[1]").click()
        print("Roles Page")


    @pytest.fixture()
    def test_e_transactions(self, test_d_roles):            #transactions
        time.sleep(5)
        self.webdriver.find_element_by_xpath("//em[contains(text(),'credit_card')]").click()
        time.sleep(5)
        self.webdriver.implicitly_wait(5000)
        self.webdriver.find_element_by_xpath("//body/div[@id='content']/div[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/section[1]/div[1]/ul[1]/li[1]/a[1]/span[1]").click()
        print("Transactions Page")


    @pytest.fixture()
    def test_f_api(self, test_e_transactions):               #api & plugins
        time.sleep(5)
        self.webdriver.find_element_by_xpath("//body/div[@id='content']/div[1]/div[1]/div[1]/main[1]/div[1]/div[1]/section[2]/div[1]/div[1]/div[7]/div[1]/div[1]/figure[1]/a[1]/span[1]/em[1]").click()
        time.sleep(5)
        self.webdriver.find_element_by_xpath("//body/div[@id='content']/div[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/section[1]/div[1]/ul[1]/li[1]/a[1]/span[1]").click()
        print("API&Plugins Page")


    def test_g_account(self,test_f_api):                     #accounts settings
        time.sleep(5)
        self.webdriver.find_element_by_xpath("//body/div[@id='content']/div[1]/div[1]/div[1]/main[1]/div[1]/div[1]/section[2]/div[1]/div[1]/div[10]/div[1]/div[1]/figure[1]/a[1]/span[1]/em[1]").click()
        time.sleep(5)
        self.webdriver.implicitly_wait(5000)
        self.webdriver.find_element_by_xpath("//body/div[@id='content']/div[1]/div[1]/div[1]/main[1]/div[1]/div[1]/section[1]/div[1]/ul[1]/li[1]/a[1]/span[1]").click()
        print("Account Settings Page")
        self.webdriver.close()
        self.webdriver.__exit__()