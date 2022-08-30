import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from pages.side_bar import SideBar
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT, DEFAULT_LOCATOR_TYPE



class ChangeLanguageTest(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    @classmethod
    def tearDown(self):
        self.driver.quit()

    def test_change_language(self):
        # login to system
        user_login = LoginPage(self.driver)
        user_login.type_in_email("user01@getnada.com")
        user_login.type_in_password("Test-1234")
        user_login.click_on_login()
        # load the dashboard page
        dashboard = Dashboard(self.driver)
        dashboard.wait_for_element_to_be_clickable(dashboard.add_player_link_xpath)
        time.sleep(3)
        # signout from system
        side_bar = SideBar(self.driver)
        language_xpath = side_bar.languages_link
        side_bar.click_on_the_element(language_xpath)
        time.sleep(3)




