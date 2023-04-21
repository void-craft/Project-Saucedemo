from behave import *
from selenium import webdriver
from pageobjects.products_page import ProductsPage


@when('the user removes the items from the cart')
def remove_items(context):
    context.products_page = ProductsPage(context.driver)
    context.products_page.add_or_remove_items(context.products_page.BUTTON_ADD_TO_CART_XPATH)


@then('the user should not see the counter')
def validate_absence_of_total_icon(context):
    cart_icon = context.products_page.is_cart_icon_present(context.products_page.COUNTER_TOTAL_ITEMS_XPATH)
    if not cart_icon:
        print("Remove items from cart test passed.")
        assert True
    else:
        print("Remove items from cart test failed.")
        assert False

