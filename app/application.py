from pages.login_page import LoginPage
from pages.settings_page import SettingsPage
from pages.sub_and_pay_page import SubAndPayPage
from pages.main_page import MainPage

class Application:

    def __init__(self, driver):
        self.main_page = MainPage(driver)
        self.sub_and_pay_page = SubAndPayPage(driver)
        self.settings_page = SettingsPage(driver)
        self.login_page = LoginPage(driver)
