# pageobjects/checkout_your_info_page.py
from selenium.webdriver.common.by import By
from pageobjects.base_page import BasePage


class CheckoutYourInformationPage(BasePage):
    CHECKOUT_INFO_TITLE = (By.CSS_SELECTOR, ".title")
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    CANCEL_BUTTON = (By.ID, "cancel")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    def __init__(self, driver):
        super().__init__(driver)

    def verify_on_checkout_info_page(self):
        """Verifies that the user is on the 'Checkout: Your Information' page."""
        self.wait_for_element(self.CHECKOUT_INFO_TITLE)
        assert self.get_text(self.CHECKOUT_INFO_TITLE) == "Checkout: Your Information", "Not on Checkout Information page."

    def enter_checkout_information(self, first_name, last_name, postal_code):
        """Enters user information for checkout."""
        self.send_keys(self.FIRST_NAME_INPUT, first_name)
        self.send_keys(self.LAST_NAME_INPUT, last_name)
        self.send_keys(self.POSTAL_CODE_INPUT, postal_code)

    def click_continue(self):
        """Clicks the 'Continue' button to proceed to checkout overview."""
        self.click_element(self.CONTINUE_BUTTON)

    def click_cancel(self):
        """Clicks the 'Cancel' button to go back to the cart."""
        self.click_element(self.CANCEL_BUTTON)

    def get_error_message(self):
        """Returns the text of the error message on the page."""
        return self.get_text(self.ERROR_MESSAGE)