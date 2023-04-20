from selenium.webdriver.common.by import By
from pageobjects.base_page import BasePage


class ProductsPage(BasePage):
    SPAN_TITLE_CSS = By.CSS_SELECTOR, "span.title"
    IMAGE_PRODUCTS_TAG = By.TAG_NAME, "img"
