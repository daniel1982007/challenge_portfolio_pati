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
        self.driver_serivce = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_serivce)
        self.driver.get('https://scouts.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)
        self.user_login = LoginPage(self.driver)
        self.dashboard = Dashboard(self.driver)

    @classmethod
    def tearDown(self):
        self.driver.quit()


    def test_login_page(self):
        # self.user_login.title_of_page()   # check page title
        # self.user_login.assert_element_text(self.user_login.header_xpath, "PANEL SKAUTINGOWY")   # check the header text element
        self.user_login.type_in_email("user01@getnada.com")
        self.user_login.type_in_password("Test-1234")
        self.user_login.click_on_login()
        time.sleep(5)
        # user_login.is_login()
        self.dashboard.title_of_page()
        self.dashboard.assert_element_text("//*[text()='Players']", "Players")   # check sidebar text - Players

    def test_login_page_with_uncorrected_credential(self):
        # self.user_login.title_of_page()
        # self.user_login.assert_element_text(self.user_login.header_xpath, "PANEL SKAUTINGOWY")
        self.user_login.type_in_email("example@example.com")
        self.user_login.type_in_password("***")
        self.user_login.click_on_login()
        time.sleep(2)
        self.user_login.is_login()