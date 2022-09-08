from pages.base_page import BasePage
from utils.settings import DEFAULT_LOCATOR_TYPE


class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//*[text()='Sign in']"
    remind_password_xpath = "//*[text()='Remind password']"
    header_xpath = "//h5"
    polski_xpath = "//li[@data-value='pl']"
    english_xpath = "//li[@data-value='en']"
    login_url = "https://scouts-test.futbolkolektyw.pl/en"
    expected_title = "Scouts panel - sign in"
    error_message = "//form/div/div[1]//span"


    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)

    def type_in_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)

    def click_on_login(self):
        self.click_on_the_element(self.sign_in_button_xpath)

    def is_login(self, locator_type=DEFAULT_LOCATOR_TYPE):
        # url = self.driver.current_url
        # assert url == "https://scouts-test.futbolkolektyw.pl/en/login?redirected=true"
        error_message = self.driver.find_element(locator_type, self.error_message)
        error_message_css_value = error_message.get_attribute('class')
        print(error_message_css_value)
        assert "Error" in error_message_css_value


    def title_of_page(self):
        assert self.get_page_title(self.login_url) == self.expected_title
