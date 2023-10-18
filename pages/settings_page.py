from selenium.webdriver.common.by import By
from pages.base_page import Page

class SettingsPage(Page):
    SUBSCRIPTION_AND_PAYMENT_BUTTON =(By.CSS_SELECTOR,'a[href="/subscription"]')

    def click_subscription_and_payments(self):
        self.wait_for_element_clickable_click(*self.SUBSCRIPTION_AND_PAYMENT_BUTTON)