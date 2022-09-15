import math
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from utils.settings import DEFAULT_LOCATOR_TYPE


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

    def wait_for_element_to_be_clickable(self, locator, locator_type=DEFAULT_LOCATOR_TYPE):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((locator_type, locator)))

    def wait_for_element_to_be_visible(self, locator, locator_type=DEFAULT_LOCATOR_TYPE):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((locator_type, locator)))

    def wait_for_element_to_be_located(self, locator, locator_type=DEFAULT_LOCATOR_TYPE):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located((locator_type, locator)))

    def wait_and_get_toastify_message(self, toastify_locator, locator_type=DEFAULT_LOCATOR_TYPE):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((locator_type, toastify_locator)))
        return element.text

    def get_input_validation_message(self, locator, locator_type=DEFAULT_LOCATOR_TYPE):
        element = self.driver.find_element(locator_type, locator)
        message = element.get_property('validationMessage')
        return message


    def get_input_error_css_value(self, locator, locator_type=DEFAULT_LOCATOR_TYPE):
        element = self.driver.find_element(locator_type, locator)
        css_value = element.get_attribute('class')
        print(css_value)
        return css_value

    def choose_an_option(self, clickable_selector, option_list_locator, position, locator_type=DEFAULT_LOCATOR_TYPE):
        self.click_on_the_element(clickable_selector)
        option_list = self.driver.find_element(locator_type, option_list_locator)
        options = option_list.find_elements(locator_type, f"{option_list_locator}//child::li")
        # for option in options:
        #     print(option.text)
        # self.wait_for_element_to_be_visible(input_selector)
        # self.field_send_keys(input_selector, legs[position].text)
        self.click_on_the_element(f"{option_list_locator}//child::li[{position}]")

    def go_to_a_player_page(self, click_times, next_or_back, arrow_locator, pagination_locator, locator_type=DEFAULT_LOCATOR_TYPE):
        # find how many players in total
        players_pagination_text = self.driver.find_element(locator_type, pagination_locator).text
        index_start = players_pagination_text.index('f')
        number_text = players_pagination_text[index_start + 2:]
        number = int(number_text)

        page_title = self.driver.title
        current_page_number_start_index = page_title.index('page') + 5
        current_page_number = int(page_title[current_page_number_start_index:])

        max_click_times = math.floor(number / 10)

        if next_or_back == 'next':
            max_click_times -= current_page_number - 1
            if click_times == 0:
                pass
            elif click_times >= max_click_times:
                for _ in range(max_click_times):
                    self.click_on_the_element(arrow_locator)
                WebDriverWait(self.driver, 10).until(EC.title_is(f'Players ({number_text}) page {max_click_times + 1}'))
            else:
                for _ in range(click_times):
                    self.click_on_the_element(arrow_locator)
                    print(current_page_number, click_times)
                    print(f'Players ({number_text}) page {current_page_number + click_times}')
                    print(self.driver.title)
                WebDriverWait(self.driver, 10).until(EC.title_is(f'Players ({number_text}) page {current_page_number + click_times}'))
        elif next_or_back == 'back':
            max_click_times = current_page_number - 1
            if click_times == 0:
                pass
            elif click_times >= max_click_times:
                for _ in range(max_click_times):
                    self.click_on_the_element(arrow_locator)
                WebDriverWait(self.driver, 10).until(EC.title_is(f'Players ({number_text}) page 1'))
            else:
                for _ in range(click_times):
                    self.click_on_the_element(arrow_locator)
                WebDriverWait(self.driver, 10).until(EC.title_is(f'Players ({number_text}) page {current_page_number - click_times}'))
