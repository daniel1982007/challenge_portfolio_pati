from pages.base_page import BasePage


class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//*[text()='Sign in']"
    remind_password_xpath = "//*[text()='Remind password']"
    header_xpath = "//h5"
    polski_xpath = "//li[@data-value='pl']"
    english_xpath = "//li[@data-value='en']"


    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)
