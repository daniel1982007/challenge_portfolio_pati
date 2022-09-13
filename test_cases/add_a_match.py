import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.add_a_match import AddAMatch
from pages.dashboard import Dashboard
from pages.edit_player_page import EditAPlayer
from pages.login_page import LoginPage
from pages.side_bar import SideBar
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT



class AddMatchTest(unittest.TestCase):

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
        self.choose_a_player = EditAPlayer(self.driver)
        self.side_bar = SideBar(self.driver)
        self.players = AddAMatch(self.driver)

    @classmethod
    def tearDown(self):
        self.driver.quit()

    def test_add_a_match(self):
        self.user_login.type_in_email("user01@getnada.com")
        self.user_login.type_in_password("Test-1234")
        self.user_login.click_on_login()
        self.dashboard.wait_for_element_to_be_clickable(self.dashboard.add_player_link_xpath)
        self.dashboard.click_on_the_element(self.side_bar.players_link)
        self.players.wait_for_element_to_be_located(self.players.players_title_path)
        # choose a player to add a match
        self.choose_a_player.get_the_player_to_be_edited(10, 8)
        self.choose_a_player.wait_for_element_to_be_visible(self.side_bar.matches_link)
        self.choose_a_player.click_on_the_element(self.side_bar.matches_link)
        self.choose_a_player.wait_for_element_to_be_clickable(self.players.add_a_match_button_path)
        self.choose_a_player.click_on_the_element(self.players.add_a_match_button_path)
        self.choose_a_player.wait_for_element_to_be_clickable(self.players.submit_button_path)
        # fill the match form required
        self.players.type_required_of_a_match('example', 'example', 0, 0, '12,31,1999')
        # fill the match form optional
        self.players.type_optional_of_a_match('red', 10, 'example', 90, 'example', 'example', 1)
        self.players.choose_home_or_out_home('home')

        time.sleep(3)

        self.choose_a_player.click_on_the_element(self.players.submit_button_path)

        time.sleep(3)

