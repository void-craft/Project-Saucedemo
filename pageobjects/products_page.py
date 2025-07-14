# pageobjects/products_page.py
from selenium.common.exceptions import TimeoutException, NoSuchElementException # Ensure NoSuchElementException is imported
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from pageobjects.base_page import BasePage


class ProductsPage(BasePage):
    SPAN_TITLE_CSS = (By.CSS_SELECTOR, "span.title")
    IMAGE_PRODUCTS_TAG = (By.CSS_SELECTOR, ".inventory_item_img img")
    SHOPPING_CART_LINK = (By.CSS_SELECTOR, ".shopping_cart_link")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "[data-test='add-to-cart-sauce-labs-backpack']")
    REMOVE_FROM_CART_BUTTON = (By.CSS_SELECTOR, "[data-test='remove-sauce-labs-backpack']")
    ALL_REMOVE_BUTTONS_BY_TEXT = (By.XPATH, "//button[text()='Remove']")
    COUNTER_TOTAL_ITEMS_XPATH = (By.XPATH, "//span[@class='shopping_cart_badge']")

    def __init__(self, driver):
        super().__init__(driver)

    def add_item_to_cart(self):
        self.click_element(self.ADD_TO_CART_BUTTON)
        
    def remove_item_from_cart(self):
        self.click_element(self.REMOVE_FROM_CART_BUTTON)

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

    def click_shopping_cart_link(self):
        self.click_element(self.SHOPPING_CART_LINK)