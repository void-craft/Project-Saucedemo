# pageobjects/shopping_cart_page.py
from selenium.webdriver.common.by import By
from pageobjects.base_page import BasePage


class ShoppingCartPage(BasePage):
    YOUR_CART_TITLE = (By.CSS_SELECTOR, ".title")
    ITEM_IN_CART_CONTAINER = (By.CSS_SELECTOR, ".cart_item")
    ITEM_NAME_IN_CART = (By.CSS_SELECTOR, ".inventory_item_name")
    ITEM_QUANTITY_IN_CART = (By.CSS_SELECTOR, ".cart_quantity")
    ITEM_PRICE_IN_CART = (By.CSS_SELECTOR, ".inventory_item_price")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CONTINUE_SHOPPING_BUTTON = (By.ID, "continue-shopping")
    REMOVE_BUTTON_IN_CART_BY_NAME_PREFIX = "remove-sauce-labs-"

    def __init__(self, driver):
        super().__init__(driver)

    def verify_on_cart_page(self):
        """Verifies that the user is on the 'Your Cart' page."""
        self.wait_for_element(self.YOUR_CART_TITLE)
        assert self.get_text(self.YOUR_CART_TITLE) == "Your Cart", "Not on Shopping Cart page."

    def get_cart_items_details(self):
        """Returns a list of dictionaries, each containing details of an item in the cart."""
        items = []
        cart_item_elements = self.wait_for_elements(self.ITEM_IN_CART_CONTAINER)
        for item_element in cart_item_elements:
            name = item_element.find_element(*self.ITEM_NAME_IN_CART).text
            quantity = int(item_element.find_element(*self.ITEM_QUANTITY_IN_CART).text)
            price = float(item_element.find_element(*self.ITEM_PRICE_IN_CART).text.replace('$', ''))
            items.append({"name": name, "quantity": quantity, "price": price})
        return items

    def click_checkout(self):
        """Clicks the 'Checkout' button to proceed to checkout information."""
        self.click_element(self.CHECKOUT_BUTTON)

    def click_continue_shopping(self):
        """Clicks the 'Continue Shopping' button."""
        self.click_element(self.CONTINUE_SHOPPING_BUTTON)
        
    def remove_item_from_cart_page_by_name(self, item_name):
        """Removes a specific item from the cart page by its name."""
        item_raw_name = item_name.lower().replace(" ", "-")
        locator_id = f"{self.REMOVE_BUTTON_IN_CART_BY_NAME_PREFIX}{item_raw_name}"
        self.click_element((By.ID, locator_id))