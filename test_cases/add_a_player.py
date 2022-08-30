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
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    @classmethod
    def tearDown(self):
        self.driver.quit()

    def test_add_a_player(self):
        user_login = LoginPage(self.driver)
        user_login.type_in_email("user01@getnada.com")
        user_login.type_in_password("Test-1234")
        user_login.click_on_login()
        dashboard = Dashboard(self.driver)
        dashboard.wait_for_element_to_be_clickable(dashboard.add_player_link_xpath)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en/players/add')
        add_player = AddAPlayer(self.driver)
        add_player.wait_for_element_to_be_clickable("//span[text()='Add player']")

        # add player info and validate info then add to database
        # fields required
        add_player.field_send_keys("//input[@name='name']", "test_test")
        add_player.field_send_keys("//input[@name='surname']", "test_test")
        add_player.field_send_keys("//input[@name='age']", "10,10,1989")
        add_player.field_send_keys("//input[@name='mainPosition']", "shooter")
        # fields optional
        add_player.field_send_keys("//input[@name='email']", "example@example.com")
        add_player.field_send_keys("//input[@name='phone']", '333333333')
        add_player.field_send_keys("//input[@name='weight']", '85')
        add_player.field_send_keys("//input[@name='height']", '185')
        add_player.choose_an_option("//div[@id='mui-component-select-leg']", "//div[@id='menu-leg']//ul", 2)
        add_player.field_send_keys("//input[@name='club']", 'example-club')
        add_player.field_send_keys("//input[@name='level']", "example")
        add_player.field_send_keys("//input[@name='secondPosition']", "guard")
        add_player.choose_an_option("//div[@id='mui-component-select-district']", "//div[@id='menu-district']//ul", 11)
        add_player.field_send_keys("//input[@name='achievements']", "Mr. football")
        # add languages
        add_player.click_on_the_element("//button[@aria-label='Add language']")
        add_player.wait_for_element_to_be_visible("//input[@name='languages[0]']")
        add_player.field_send_keys("//input[@name='languages[0]']", "English")
        # add social media links
        add_player.field_send_keys("//input[@name='webLaczy']", "example-link")
        add_player.field_send_keys("//input[@name='web90']", "web90-link")
        add_player.field_send_keys("//input[@name='webFB']", "webFB-link")
        # add youtube channel
        add_player.click_on_the_element("//button[@aria-label='Add link to Youtube']")
        add_player.wait_for_element_to_be_visible("//input[@name='webYT[0]']")
        add_player.field_send_keys("//input[@name='webYT[0]']", "")
        # set a time break
        time.sleep(4)
        # validation of the required fields
        add_player.validate_input_field("//input[@name='name']//parent::div")
        add_player.validate_input_field("//input[@name='surname']//parent::div")
        add_player.validate_input_field("//input[@name='age']//parent::div")
        add_player.validate_input_field("//input[@name='mainPosition']//parent::div")
        # add info to database
        add_player.add_a_player_to_database("//button[@type='submit']")

