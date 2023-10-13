from pages.base_page import Page
from selenium.webdriver.common.by import By


class MainPage(Page):

    SETTING_OPTION = (By.CSS_SELECTOR, 'a[href="/settings"].menu-button-block.w-inline-block')

    def click_settings_option(self):
        self.click(*self.SETTING_OPTION)

