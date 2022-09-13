import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from pages.side_bar import SideBar
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT, DEFAULT_LOCATOR_TYPE



class LogoutTest(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://scouts.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)
        self.user_login = LoginPage(self.driver)
        self.dashboard = Dashboard(self.driver)
        self.side_bar = SideBar(self.driver)


    @classmethod
    def tearDown(self):
        self.driver.quit()

    def test_logout_from_system(self):
        # login to system
        self.user_login.type_in_email("user01@getnada.com")
        self.user_login.type_in_password("Test-1234")
        self.user_login.click_on_login()
        # load the dashboard page
        self.dashboard.wait_for_element_to_be_clickable(self.dashboard.add_player_link_xpath)
        time.sleep(2)
        self.side_bar.click_on_the_element(self.side_bar.signout_link)
        time.sleep(2)




