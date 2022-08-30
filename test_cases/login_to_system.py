import os
import time
import unittest
from selenium import webdriver

from selenium.webdriver.chrome.service import Service

from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class LoginPageTest(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        # self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver_serivce = Service(executable_path=DRIVER_PATH)

        self.driver = webdriver.Chrome(service=self.driver_serivce)

        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    @classmethod
    def tearDown(self):
        self.driver.quit()


    def test_login_page(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()   # check page title
        user_login.assert_element_text("//h5[text()='Scouts Panel']", "Scouts Panel")   # check the header text element
        user_login.type_in_email("user01@getnada.com")
        user_login.type_in_password("Test-1234")
        user_login.click_on_login()
        time.sleep(5)
        user_login.is_login()
        dashboard = Dashboard(self.driver)
        dashboard.title_of_page()
        dashboard.assert_element_text("//*[text()='Players']", "Players")   # check sidebar text - Players