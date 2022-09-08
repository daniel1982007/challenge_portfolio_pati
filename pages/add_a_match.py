from pages.base_page import BasePage


class AddAMatch(BasePage):
    players_title_path = "//title[starts-with(., 'Players')]"
    add_a_match_button_path = "//span[text()='Add match']//parent::button"
    submit_button_path = "//span[text()='Submit']/parent::button"
    my_team_input_path = "//input[@name='myTeam']"
    enemy_team_input_path = "//input[@name='enemyTeam']"
    my_team_score_path = "//input[@name='myTeamScore']"
    enemy_team_score_path = "//input[@name='enemyTeamScore']"
    date_path = "//input[@name='date']"
    tshirt_path = "//input[@name='tshirt']"
    number_path = "//input[@name='number']"
    league_path = "//input[@name='league']"
    time_played_path = "//input[@name='timePlayed']"
    webmatch_path = "//input[@name='webMatch']"
    general_path = "//input[@name='general']"
    rating_path = "//input[@name='rating']"
    home_path = "//fieldset//label[1]"
    out_home_path = "//fieldset//label[2]"



    def type_required_of_a_match(self, my_team_name, enemy_team_name, my_score, enemy_score, date):
        self.field_send_keys(self.my_team_input_path, my_team_name)
        self.field_send_keys(self.enemy_team_input_path, enemy_team_name)
        self.field_send_keys(self.my_team_score_path, my_score)
        self.field_send_keys(self.enemy_team_score_path, enemy_score)
        self.field_send_keys(self.date_path, date)

    def type_optional_of_a_match(self, color, number, league, time_in_total, webmatch, general, rating):
        self.field_send_keys(self.tshirt_path, color)
        self.field_send_keys(self.number_path, number)
        self.field_send_keys(self.league_path, league)
        self.field_send_keys(self.time_played_path, time_in_total)
        self.field_send_keys(self.webmatch_path, webmatch)
        self.field_send_keys(self.general_path, general)
        self.field_send_keys(self.rating_path, rating)

    def choose_home_or_out_home(self, option):
        if option == 'home':
            self.click_on_the_element(self.home_path)
        else:
            self.click_on_the_element(self.out_home_path)
