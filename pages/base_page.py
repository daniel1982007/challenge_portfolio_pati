from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage():

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def field_send_keys(self, selector, value, locator_type=By.XPATH):
        return self.driver.find_element(locator_type, selector).send_keys(value)

    def click_on_the_element(self, selector, selector_type=By.XPATH):
        return self.driver.find_element(selector_type, selector).click()

    def get_page_title(self, url):
        self.driver.get(url)
        return self.driver.title

    def assert_element_text(self, xpath, expected_text):
        element = self.driver.find_element(by=By.XPATH, value=xpath)
        element_text = element.text

        # print out element_text
        print(element_text)

        assert element_text == expected_text
