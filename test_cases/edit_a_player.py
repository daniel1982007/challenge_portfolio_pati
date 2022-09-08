import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.edit_player_page import EditAPlayer
from pages.login_page import LoginPage
from pages.side_bar import SideBar
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT



class EditPlayerTest(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)
        self.user_login = LoginPage(self.driver)
        self.edit_player = EditAPlayer(self.driver)
        self.side_bar = SideBar(self.driver)

    @classmethod
    def tearDown(self):
        self.driver.quit()

    def test_edit_a_player(self):
        self.user_login.type_in_email("user01@getnada.com")
        self.user_login.type_in_password("Test-1234")
        self.user_login.click_on_login()
        self.side_bar.wait_for_element_to_be_visible(self.side_bar.players_link)
        self.edit_player.get_the_player_to_be_edited(15, 9)
        self.edit_player.wait_for_element_to_be_located(self.edit_player.edit_player_title_path)   # test change to title

        self.edit_player.edit_player_field(self.edit_player.name_path, "real name")
        self.edit_player.edit_player_field(self.edit_player.main_position_path, "main position")
        time.sleep(3)

        self.edit_player.update_player_to_database(self.edit_player.submit_button_path)
        time.sleep(3)

