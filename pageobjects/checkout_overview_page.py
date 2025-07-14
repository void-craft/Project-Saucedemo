# pageobjects/checkout_overview_page.py
from selenium.webdriver.common.by import By
from pageobjects.base_page import BasePage


class CheckoutOverviewPage(BasePage):
    # Locators
    CHECKOUT_OVERVIEW_TITLE = (By.CSS_SELECTOR, ".title")
    CART_ITEM_LABEL = (By.CSS_SELECTOR, ".cart_item_label")
    PAYMENT_INFO_LABEL = (By.CSS_SELECTOR, ".summary_info_label:nth-child(2)")
    SHIPPING_INFO_LABEL = (By.CSS_SELECTOR, ".summary_info_label:nth-child(4)")
    ITEM_TOTAL_LABEL = (By.CSS_SELECTOR, ".summary_subtotal_label")
    TAX_LABEL = (By.CSS_SELECTOR, ".summary_tax_label")
    TOTAL_LABEL = (By.CSS_SELECTOR, ".summary_total_label")
    FINISH_BUTTON = (By.ID, "finish")
    CANCEL_BUTTON = (By.ID, "cancel")

    def __init__(self, driver):
        super().__init__(driver)

    def verify_on_checkout_overview_page(self):
        """Verifies that the user is on the 'Checkout: Overview' page."""
        self.wait_for_element(self.CHECKOUT_OVERVIEW_TITLE)
        assert self.get_text(self.CHECKOUT_OVERVIEW_TITLE) == "Checkout: Overview", "Not on Checkout Overview page."

    def verify_item_in_overview(self, item_name):
        """Verifies a specific item is listed in the checkout overview."""
        item_locator = (By.XPATH, f"//div[@class='inventory_item_name' and text()='{item_name}']")
        return self.is_element_displayed(item_locator)

    def get_total_price(self):
        """Returns the total price displayed on the overview page."""
        total_text = self.get_text(self.TOTAL_LABEL)
        return float(total_text.replace("Total: $", ""))

    def click_finish(self):
        """Clicks the 'Finish' button to complete the order."""
        self.click_element(self.FINISH_BUTTON)

    def click_cancel(self):
        """Clicks the 'Cancel' button to go back to the products page."""
        self.click_element(self.CANCEL_BUTTON)