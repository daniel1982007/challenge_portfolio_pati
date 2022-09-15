import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.add_a_match_form_page import AddAMatchForm
from pages.add_a_match_page import AddAMatch
from pages.dashboard import Dashboard
from pages.edit_player_page import EditAPlayer
from pages.login_page import LoginPage
from pages.players_page import PlayersPage
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
        self.add_a_match = AddAMatch(self.driver)
        self.add_a_match_form = AddAMatchForm(self.driver)
        self.side_bar = SideBar(self.driver)
        self.players = PlayersPage(self.driver)

    @classmethod
    def tearDown(self):
        self.driver.quit()

    def test_add_a_match(self):
        self.user_login.type_in_email("user01@getnada.com")
        self.user_login.type_in_password("Test-1234")
        self.user_login.click_on_login()
        self.dashboard.wait_for_element_to_be_clickable(self.dashboard.add_player_link_xpath)
        self.dashboard.click_on_the_element(self.side_bar.players_link)
        self.players.wait_player_page_title()
        # choose a player to add a match
        self.players.get_the_player_to_be_edited(5)
        self.choose_a_player.wait_for_edit_player_title()
        # self.choose_a_player.get_the_player_to_be_edited(10, 8)
        self.side_bar.click_on_the_element(self.side_bar.matches_link)
        self.add_a_match.wait_for_add_a_match_title()
        self.add_a_match.click_on_the_element(self.add_a_match.add_a_match_button_path)
        self.add_a_match_form.wait_for_add_a_match_form_title()
        # fill the match form required
        self.add_a_match_form.type_required_of_a_match('example', 'example', 0, 0, '12,31,1999')
        # fill the match form optional
        self.add_a_match_form.type_optional_of_a_match('red', 10, 'example', 90, 'example', 'example', 1)
        self.add_a_match_form.choose_home_or_out_home('home')
        time.sleep(3)
        self.add_a_match_form.click_on_the_element(self.add_a_match_form.submit_button_path)
        time.sleep(3)

    def test_add_a_match_on_further_page(self):
        self.user_login.type_in_email("user01@getnada.com")
        self.user_login.type_in_password("Test-1234")
        self.user_login.click_on_login()
        self.dashboard.wait_for_element_to_be_clickable(self.dashboard.add_player_link_xpath)
        self.dashboard.click_on_the_element(self.side_bar.players_link)
        self.players.wait_player_page_title()
        # choose a player to add a match
        self.players.go_to_a_player_page(20, 'next', self.players.next_page_arrow_path, self.players.pagination_path)
        self.players.go_to_a_player_page(10, 'back', self.players.back_page_arrow_path, self.players.pagination_path)
        self.players.get_the_player_to_be_edited(5)
        self.choose_a_player.wait_for_edit_player_title()
        # self.choose_a_player.get_the_player_to_be_edited(10, 8)
        self.side_bar.click_on_the_element(self.side_bar.matches_link)
        self.add_a_match.wait_for_add_a_match_title()
        self.add_a_match.click_on_the_element(self.add_a_match.add_a_match_button_path)
        self.add_a_match_form.wait_for_add_a_match_form_title()
        # fill the match form required
        self.add_a_match_form.type_required_of_a_match('example', 'example', 0, 0, '12,31,1999')
        # fill the match form optional
        self.add_a_match_form.type_optional_of_a_match('red', 10, 'example', 90, 'example', 'example', 1)
        self.add_a_match_form.choose_home_or_out_home('home')
        time.sleep(3)
        self.add_a_match_form.click_on_the_element(self.add_a_match_form.submit_button_path)
        time.sleep(3)

