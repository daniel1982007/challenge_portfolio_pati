import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.add_player_page import AddAPlayer
from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT



class AddPlayerTest(unittest.TestCase):

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
        self.add_player = AddAPlayer(self.driver)


    @classmethod
    def tearDown(self):
        self.driver.quit()

    def test_add_a_player(self):
        self.user_login.type_in_email("user01@getnada.com")
        self.user_login.type_in_password("Test-1234")
        self.user_login.click_on_login()
        self.dashboard.wait_for_element_to_be_clickable(self.dashboard.add_player_link_xpath)
        self.dashboard.click_on_the_element(self.dashboard.add_player_link_xpath)
        self.add_player.wait_for_element_to_be_visible(self.add_player.add_player_header)

        # add player info and validate info then add to database
        # fields required
        self.add_player.type_in_required_fields("test_test", "test_test", "10,10,1989", "shooter")
        # fields optional
        self.add_player.type_in_optional_fields("example@example.com")
        # fields optional choose an option
        self.add_player.choose_a_leg(2)
        self.add_player.choose_a_district(8)
        # add languages
        self.add_player.add_a_language(0, 'German')     # input index starts from 0
        self.add_player.add_a_language(1, 'English')
        self.add_player.add_a_language(2, 'Polish')
        # add social media
        self.add_player.add_social_media('new-link', 'new-link')
        # add youtube channel
        self.add_player.add_youtube_channel(0, 'myfirstyoutubechannel')     # input index starts from 0
        self.add_player.add_youtube_channel(1, 'mysecondyoutubechannel')
        # set a time break
        time.sleep(3)
        # add info to database
        self.add_player.add_a_player_to_database("//button[@type='submit']")
        self.add_player.new_player_should_be_added_to_database()
        time.sleep(1)


    def test_add_a_player_with_invalid_data(self):
        self.user_login.type_in_email("user01@getnada.com")
        self.user_login.type_in_password("Test-1234")
        self.user_login.click_on_login()
        self.dashboard.wait_for_element_to_be_clickable(self.dashboard.add_player_link_xpath)
        self.dashboard.click_on_the_element(self.dashboard.add_player_link_xpath)
        self.add_player.wait_for_element_to_be_visible(self.add_player.add_player_header)
        # fields required
        self.add_player.type_in_required_fields("test_test", "test_test", "12,dd,yyyy", "shooter")
        self.add_player.click_on_the_element(self.add_player.submit_button)
        time.sleep(2)
        self.add_player.required_fields_should_not_pass()