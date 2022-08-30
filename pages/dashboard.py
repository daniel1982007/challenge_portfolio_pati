from pages.base_page import BasePage


class Dashboard(BasePage):
    header_xpath = "//h6[text()='Scouts Panel']"
    main_page_nav_xpath = "//*[text()='Main page']"
    main_page_nav_icon_xpath = "//*[text()='Main page']//parent::div//preceding-sibling::div//*[local-name()='svg']"
    players_nav_xpath = "//*[text()='Players']"
    players_nav_icon_xpath = "//*[text()='Players']//parent::div//preceding-sibling::div//*[local-name()='svg']"
    polski_nav_xpath = "//*[text()='Polski']"
    polski_nav_icon_xpath = "//*[text()='Polski']//parent::div//preceding-sibling::div//*[local-name()='svg']"
    sign_out_nav_xpath = "//*[text()='Sign out']"
    sign_out_nav_icon_xpath = "//*[text()='Sign out']//parent::div//preceding-sibling::div//*[local-name()='svg']"
    players_count_header_xpath = "//*[text()='Players count']"
    players_count_number_xpath = "//*[text()='Players count']//following-sibling::div//b"
    scouts_panel_bg_xpath = "//*[contains(@title, 'Logo')]"
    scouts_panel_header_xpath = "//h2[text()='Scouts Panel']"
    scouts_panel_description_xpath = "//h2[text()='Scouts Panel']//following-sibling::p"
    dev_team_link_xpath = "//*[contains(@target, '_blank')]"
    add_player_link_xpath = "//a[@href='/en/players/add']"
    last_created_player_link_xpath = "//*[text()='Last created player']//following-sibling::a[1]"
    last_updated_player_link_xpath = "//*[text()='Last updated player']//following-sibling::a[1]"
    last_updated_report_link_xpath = "//*[text()='Last updated report']//following-sibling::a[1]"

    dashboard_url = "https://scouts-test.futbolkolektyw.pl/"
    expected_title = "Scouts panel"

    def title_of_page(self):
        # self.wait_for_element_to_be_clickable(self.scouts_panel_bg_xpath)
        self.wait_for_element_to_be_clickable(self.players_count_number_xpath)
        assert self.get_page_title(self.dashboard_url) == self.expected_title