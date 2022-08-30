from pages.base_page import BasePage


class SideBar(BasePage):

    main_page_link = "//span[text()='Main page']/parent::div/parent::div"
    players_link = "//span[text()='Players']/parent::div/parent::div"
    player_link = "//div[@role='presentation']//child::ul[2]/div[1]"
    matches_link = "//div[@role='presentation']//child::ul[2]/div[2]"
    reports_link = "//div[@role='presentation']//child::ul[2]/div[3]"
    languages_link = "//div[@role='presentation']//child::ul[last()]/div"
    signout_link = "//div[@role='presentation']//child::ul[last()]/div[2]"