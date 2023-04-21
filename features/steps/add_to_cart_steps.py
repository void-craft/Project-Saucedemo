import time

from behave import *
from selenium import webdriver
from pageobjects.login_page import LoginPage
from pageobjects.products_page import ProductsPage


@when('the user enters the username "standard_user"')
def enter_username(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.enter_username(context.login_page.STANDARD_USERNAME)


@when('the user adds the items to the cart')
def add_items(context):
    context.products_page = ProductsPage(context.driver)
    context.products_page.add_or_remove_items(context.products_page.BUTTON_ADD_TO_CART_XPATH)


@then('the user should see the total number of cart items')
def validate_total_items(context):
    time.sleep(3)
    cart_icon = context.products_page.is_cart_icon_present(context.products_page.COUNTER_TOTAL_ITEMS_XPATH)
    if cart_icon:
        print("Add to cart test passed.")
        assert True
    else:
        print("Add to cart test failed.")
        assert False


