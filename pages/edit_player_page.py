import time

from selenium.webdriver import Keys

from pages.base_page import BasePage
from utils.settings import DEFAULT_LOCATOR_TYPE


class EditAPlayer(BasePage):

    def get_the_player_to_be_edited(self, page, row, locator_type=DEFAULT_LOCATOR_TYPE):
        url = f"https://scouts-test.futbolkolektyw.pl/en/players?lng=en&subpath=en&start={page}"
        self.driver.get(url)
        player_locator = f"//tr[@id='MUIDataTableBodyRow-{row}']"
        player_to_be_edit = self.driver.find_element(locator_type, player_locator)
        player_to_be_edit.click()

    def edit_player_field(self, locator, value, locator_type=DEFAULT_LOCATOR_TYPE):
        input_field = self.driver.find_element(locator_type, locator)
        print(input_field.get_attribute('value'))
        input_field.send_keys(Keys.CONTROL, 'a')
        time.sleep(1)
        # input_field.clear()
        self.field_send_keys(locator, value)

    def update_player_to_database(self, submit_button_locator):
        self.click_on_the_element(submit_button_locator)