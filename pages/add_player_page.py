import time

from pages.base_page import BasePage
from utils.settings import DEFAULT_LOCATOR_TYPE


class AddAPlayer(BasePage):
    add_player_header = "//span[text()='Add player']"
    name_path = "//input[@name='name']"
    surname_path = "//input[@name='surname']"
    age_path = "//input[@name='age']"
    main_position_path = "//input[@name='mainPosition']"
    name_error_path = "//input[@name='name']/parent::div"
    surname_error_path = "//input[@name='surname']/parent::div"
    age_error_path = "//input[@name='age']/parent::div"
    main_position_error_path = "//input[@name='mainPosition']/parent::div"
    email_path = "//input[@name='email']"
    phone_path = "//input[@name='phone']"
    weight_path = "//input[@name='weight']"
    height_path = "//input[@name='height']"
    club_path = "//input[@name='club']"
    level_path = "//input[@name='level']"
    second_position_path = "//input[@name='secondPosition']"
    achievements_path = "//input[@name='achievements']"
    add_language_button_path = "//button[@aria-label='Add language']"
    football_path = "//input[@name='webLaczy']"
    ninty_minutes_path = "//input[@name='web90']"
    facebook_path = "//input[@name='webFB']"
    add_youtube_button_path = "//button[@aria-label='Add link to Youtube']"
    choose_leg_path = "//input[@name='leg']/parent::div"
    choose_district_path = "//input[@name='district']/parent::div"
    options_list_path = "//ul[@role='listbox']"

    def type_in_required_fields(self, name, surname, age, main_position):
        self.field_send_keys(self.name_path, name)
        self.field_send_keys(self.surname_path, surname)
        self.field_send_keys(self.age_path, age)
        self.field_send_keys(self.main_position_path, main_position)

    def type_in_optional_fields(self, email="", phone="", weight="", height="", club="", level="", second_position="", achievements=""):
        self.field_send_keys(self.email_path, email)
        self.field_send_keys(self.phone_path, phone)
        self.field_send_keys(self.weight_path, weight)
        self.field_send_keys(self.height_path, height)
        self.field_send_keys(self.club_path, club)
        self.field_send_keys(self.level_path, level)
        self.field_send_keys(self.second_position_path, second_position)
        self.field_send_keys(self.achievements_path, achievements)

    def choose_a_leg(self, position):
        self.choose_an_option(self.choose_leg_path, self.options_list_path, position)

    def choose_a_district(self, position):
        self.choose_an_option(self.choose_district_path, self.options_list_path, position)

    def add_a_language(self, order, language=""):
        self.click_on_the_element(self.add_language_button_path)
        new_language_input_path = f"//input[@name='languages[{order}]']"
        self.wait_for_element_to_be_visible(new_language_input_path)
        self.field_send_keys(new_language_input_path, language)

    def add_social_media(self, football="", ninty_minutes="", facebook=""):
        self.field_send_keys(self.football_path, football)
        self.field_send_keys(self.ninty_minutes_path, ninty_minutes)
        self.field_send_keys(self.facebook_path, facebook)

    def add_youtube_channel(self, order, youtube_link=""):
        self.click_on_the_element(self.add_youtube_button_path)
        new_youtube_channel_input_path = f"//input[@name='webYT[{order}]']"
        self.wait_for_element_to_be_visible(new_youtube_channel_input_path)
        self.field_send_keys(new_youtube_channel_input_path, youtube_link)

    def add_a_player_to_database(self, submit_button_selector):
        self.click_on_the_element(submit_button_selector)

    def validate_all_required_fields(self):
        name_error_css_value = self.get_input_error_css_value(self.name_error_path)
        surname_error_css_value = self.get_input_error_css_value(self.surname_error_path)
        age_error_css_value = self.get_input_error_css_value(self.age_error_path)
        main_position_error_css_value = self.get_input_error_css_value(self.main_position_error_path)
        css_value = name_error_css_value + surname_error_css_value + age_error_css_value + main_position_error_css_value
        print(css_value)
        assert 'error' in css_value