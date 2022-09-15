import time

from selenium.webdriver import Keys

from pages.base_page import BasePage
from utils.settings import DEFAULT_LOCATOR_TYPE


class EditAPlayer(BasePage):
    edit_player_title_path = "//title[starts-with(., 'Edit player')]"
    name_path = "//input[@name='name']"
    main_position_path = "//input[@name='mainPosition']"
    submit_button_path = "//button[@type='submit']"
    toastify_path = "//div[@class='Toastify']"


    def wait_for_edit_player_title(self):
        self.wait_for_element_to_be_located(self.edit_player_title_path)

    def edit_player_field(self, locator, value, locator_type=DEFAULT_LOCATOR_TYPE):
        input_field = self.driver.find_element(locator_type, locator)
        print(input_field.get_attribute('value'))
        input_field.send_keys(Keys.CONTROL, 'a')
        time.sleep(1)
        # input_field.clear()
        self.field_send_keys(locator, value)

    def update_player_to_database(self):
        self.click_on_the_element(self.submit_button_path)
        # wait for toastify message and check if successful
        toastify_text = self.wait_and_get_toastify_message(self.toastify_path)
        assert "Saved player." in toastify_text





    # def get_the_player_to_be_edited_by_url(self, page, row, locator_type=DEFAULT_LOCATOR_TYPE):
    #     url = f"https://scouts.futbolkolektyw.pl/en/players?lng=en&subpath=en&start={page}"
    #     self.driver.get(url)
    #     player_locator = f"//tr[@id='MUIDataTableBodyRow-{row}']"
    #     player_to_be_edit = self.driver.find_element(locator_type, player_locator)
    #     player_to_be_edit.click()