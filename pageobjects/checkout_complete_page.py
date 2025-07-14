# pageobjects/checkout_complete_page.py
from selenium.webdriver.common.by import By
from pageobjects.base_page import BasePage


class CheckoutCompletePage(BasePage):
    CHECKOUT_COMPLETE_TITLE = (By.CSS_SELECTOR, ".title")
    THANK_YOU_HEADER = (By.CSS_SELECTOR, ".complete-header")
    PONY_EXPRESS_IMAGE = (By.CSS_SELECTOR, ".pony_express")
    BACK_HOME_BUTTON = (By.ID, "back-to-products")

    def __init__(self, driver):
        super().__init__(driver)

    def verify_on_checkout_complete_page(self):
        self.wait_for_element(self.CHECKOUT_COMPLETE_TITLE)
        assert self.get_text(self.CHECKOUT_COMPLETE_TITLE) == "Checkout: Complete!", "Not on Checkout Complete page."

    def get_thank_you_message(self):
        return self.get_text(self.THANK_YOU_HEADER)

    def click_back_home(self):
        self.click_element(self.BACK_HOME_BUTTON)