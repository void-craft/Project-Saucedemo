from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from pageobjects.base_page import BasePage


class ProductsPage(BasePage):
    SPAN_TITLE_CSS = By.CSS_SELECTOR, "span.title"
    IMAGE_PRODUCTS_TAG = By.TAG_NAME, "img"
    BUTTON_ADD_TO_CART_XPATH = By.XPATH, "//button[@Class]"
    COUNTER_TOTAL_ITEMS_XPATH = By.XPATH, "//span[@class='shopping_cart_badge']"

    def add_or_remove_items(self, button_locator):
        buttons = self.wait_for_elements(button_locator)
        for button in buttons:
            button.click()

    def is_cart_icon_present(self, cart_icon):
        try:
            self.wait_for_element(cart_icon, timeout=2)
            return True
        except TimeoutException:
            return False

    def remove_items_from_cart(self, button_locator):
        buttons = self.wait_for_elements(button_locator)
        for button in buttons:
            button.click()
