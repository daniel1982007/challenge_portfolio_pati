from pages.base_page import BasePage


class AddAMatch(BasePage):
    add_a_match_title_path = "//title[starts-with(., 'Matches player')]"
    add_a_match_button_path = "//span[text()='Add match']//parent::button"


    def wait_for_add_a_match_title(self):
        self.wait_for_element_to_be_located(self.add_a_match_title_path)