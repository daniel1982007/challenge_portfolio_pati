import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.edit_player_page import EditAPlayer
from pages.login_page import LoginPage
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

    @classmethod
    def tearDown(self):
        self.driver.quit()

    def test_edit_a_player(self):
        user_login = LoginPage(self.driver)
        user_login.type_in_email("user01@getnada.com")
        user_login.type_in_password("Test-1234")
        user_login.click_on_login()

        edit_player = EditAPlayer(self.driver)
        edit_player.wait_for_element_to_be_visible("//span[text()='Players']")
        edit_player.get_the_player_to_be_edited(15, 9)
        time.sleep(3)
        edit_player.edit_player_field("//input[@name='name']", "real name")
        edit_player.edit_player_field("//input[@name='mainPosition']", "real surname")
        time.sleep(3)

        edit_player.validate_input_field("//input[@name='name']//parent::div")
        edit_player.validate_input_field("//input[@name='surname']//parent::div")
        edit_player.validate_input_field("//input[@name='age']//parent::div")
        edit_player.validate_input_field("//input[@name='mainPosition']//parent::div")

        edit_player.update_player_to_database("//button[@type='submit']")
        time.sleep(5)

