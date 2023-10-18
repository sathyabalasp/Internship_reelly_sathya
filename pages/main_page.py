from pages.base_page import Page
from selenium.webdriver.common.by import By


class MainPage(Page):

    SETTING_OPTION = (By.XPATH, '//div[text()="Settings"][@class="menu-button-text"]')
    INPUT_SEARCH = (By.ID,"field-6")

    def click_settings_option(self):
      self.wait_for_element_clickable_click(*self.SETTING_OPTION)




