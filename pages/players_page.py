from pages.base_page import BasePage


class PlayersPage(BasePage):
    title_path = "//title[starts-with(text(), 'Players')]"
    next_page_arrow_path = "//button[@id='pagination-next']"
    back_page_arrow_path = "//button[@id='pagination-back']"
    pagination_path = "//tfoot//p"
    player_row_path = "//tbody//tr"

    def wait_player_page_title(self):
        self.wait_for_element_to_be_located(self.title_path)

    def go_to_the_player_page_by_click_pagaination(self, click_times, next_or_back, arrow_locator):
        self.go_to_a_player_page(click_times, next_or_back, arrow_locator, self.pagination_path)

    def get_the_player_to_be_edited(self, row):
        self.click_on_the_element(f'{self.player_row_path}[{row}]')