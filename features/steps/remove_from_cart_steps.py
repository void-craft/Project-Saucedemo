# features/steps/remove_from_cart_steps.py
from behave import *
from pageobjects.products_page import ProductsPage

@when('the user removes the items from the cart')
def remove_items(context):
    context.products_page.remove_all_items_from_cart()


@then('the user should not see the counter')
def validate_absence_of_total_icon(context):
    assert context.products_page.is_cart_badge_not_present(), \
        "Cart badge is still visible after removing items, but it should not be."