import time

from pages.base_page import BasePage
from utils.settings import DEFAULT_LOCATOR_TYPE


class AddAPlayer(BasePage):

    def add_a_player_to_database(self, submit_button_selector):
        self.click_on_the_element(submit_button_selector)