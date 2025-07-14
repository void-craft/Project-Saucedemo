from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from pageobjects.base_page import BasePage


class ProductsPage(BasePage):
    SPAN_TITLE_CSS = (By.CSS_SELECTOR, "span.title")
    IMAGE_PRODUCTS_TAG = (By.CSS_SELECTOR, ".inventory_item_img img")
    ADD_TO_CART_BUTTON_PREFIX = "add-to-cart-"
    REMOVE_BUTTON_PREFIX = "remove-"
    COUNTER_TOTAL_ITEMS_XPATH = (By.XPATH, "//span[@class='shopping_cart_badge']")

    def __init__(self, driver):
        super().__init__(driver)

    def add_item_to_cart_by_name(self, item_raw_name):
        data_test_value = f"{self.ADD_TO_CART_BUTTON_PREFIX}{item_raw_name}"
        locator = (By.ID, data_test_value)
        self.click_element(locator)


    def remove_item_from_cart_by_name(self, item_raw_name):
        data_test_value = f"{self.REMOVE_BUTTON_PREFIX}{item_raw_name}"
        locator = (By.ID, data_test_value)
        self.click_element(locator)


    def remove_all_items_from_cart(self):
        ALL_REMOVE_BUTTONS = (By.XPATH, "//button[text()='Remove']")
        try:
            buttons = self.wait_for_elements(ALL_REMOVE_BUTTONS, timeout=5)
            for button in buttons:
                button.click()
        except TimeoutException:
            print("No 'Remove' buttons found on the page to click.")

    def get_cart_item_count(self):
        try:
            badge_element = self.wait_for_element(self.COUNTER_TOTAL_ITEMS_XPATH, timeout=5)
            if badge_element.text:
                return int(badge_element.text)
            return 0
        except (TimeoutException, ValueError):
            return 0

    def is_cart_badge_present(self):
        return self.is_element_displayed(self.COUNTER_TOTAL_ITEMS_XPATH, timeout=2)

    def is_cart_badge_not_present(self):
        try:
            WebDriverWait(self.driver, 5).until(
                ec.invisibility_of_element_located(self.COUNTER_TOTAL_ITEMS_XPATH)
            )
            return True
        except TimeoutException:
            return False