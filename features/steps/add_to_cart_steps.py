# features/steps/add_to_cart_steps.py
from behave import *
from pageobjects.login_page import LoginPage
from pageobjects.products_page import ProductsPage
from pageobjects.base_page import BasePage


@when('the user enters the username "standard_user"')
def enter_username(context):
    context.login_page.enter_username(context.login_page.STANDARD_USERNAME)


@when('the user adds the items to the cart')
def add_items(context):
    context.products_page.add_item_to_cart()

@then('the user should see the total number of cart items')
def validate_total_items(context):
    actual_count = context.products_page.get_cart_item_count()
    expected_count = 1
    assert actual_count > 0, "Cart badge is not visible or shows 0 items."
    assert actual_count == expected_count, \
        f"Expected {expected_count} item(s) in cart, but found {actual_count}."

    print(f"Add to cart test passed. Cart count: {actual_count}.")