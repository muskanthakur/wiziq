from webbrowser import Chrome
import pytest
import time
from Test_login import *

@pytest.mark.run(order=6)
class Test_java(Test_login):

    @pytest.fixture()
    def test_a_java(self, Test_a_login):
        time.sleep(2)
        self.webdriver.get("https://jacksparow.wiziqxt.com/admin/live-class/create")