from selenium.webdriver.common.by import By
from pages.base_page import Page

class SubAndPayPage(Page):

    SUBSCRIPTION_AND_PAYMENT_TEXT = (By.CSS_SELECTOR, '.lotion-your-h3--price.size')
    UPGRADE_PLAN_BUTTON = (By.CSS_SELECTOR, 'a[wized="upgradePlanButton"]')
    BACK_BUTTON = (By.CSS_SELECTOR, '.next-step--.black')

    def verify_sub_and_pay_page(self,expected_text):
        self.verify_text(expected_text, *self.SUBSCRIPTION_AND_PAYMENT_TEXT)

    def verify_sub_and_pay_visible(self):
        self.wait_for_element_appear(*self.SUBSCRIPTION_AND_PAYMENT_TEXT)

    def verify_upgrade_plan_buttons(self,expected_text):
        self.verify_text(expected_text, *self.UPGRADE_PLAN_BUTTON)


    def verify_back_buttons_available(self,expected_text):
        self.verify_text(expected_text, *self.BACK_BUTTON)


