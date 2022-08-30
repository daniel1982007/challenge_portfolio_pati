import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.add_player_page import AddAPlayer
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
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    @classmethod
    def tearDown(self):
        self.driver.quit()

    def test_add_a_match(self):
        user_login = LoginPage(self.driver)
        user_login.type_in_email("user01@getnada.com")
        user_login.type_in_password("Test-1234")
        user_login.click_on_login()
        dashboard = Dashboard(self.driver)
        dashboard.wait_for_element_to_be_clickable(dashboard.add_player_link_xpath)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en/players')
        time.sleep(3)
        # choose a player to add a match
        choose_a_player = EditAPlayer(self.driver)
        choose_a_player.get_the_player_to_be_edited(10, 8)
        side_bar = SideBar(self.driver)
        choose_a_player.wait_for_element_to_be_visible(side_bar.matches_link)
        choose_a_player.click_on_the_element(side_bar.matches_link)
        choose_a_player.wait_for_element_to_be_clickable("//span[text()='Add match']//parent::button")
        choose_a_player.click_on_the_element("//span[text()='Add match']//parent::button")
        choose_a_player.wait_for_element_to_be_clickable("//span[text()='Submit']/parent::button")
        # fill the match form
        choose_a_player.field_send_keys("//input[@name='myTeam']", "example team1")
        choose_a_player.field_send_keys("//input[@name='enemyTeam']", "example team2")
        choose_a_player.field_send_keys("//input[@name='myTeamScore']", 0)
        choose_a_player.field_send_keys("//input[@name='enemyTeamScore']", 0)
        choose_a_player.field_send_keys("//input[@name='date']", "08/30/2022")
        choose_a_player.click_on_the_element("//label[@type='radio'][1]")
        choose_a_player.field_send_keys("//input[@name='tshirt']", 'red')
        choose_a_player.field_send_keys("//input[@name='number']", 7)

        time.sleep(3)

        choose_a_player.click_on_the_element("//span[text()='Submit']/parent::button")

        time.sleep(3)

