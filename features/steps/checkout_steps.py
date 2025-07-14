# features/steps/checkout_steps.py
from behave import *
from pageobjects.products_page import ProductsPage
from pageobjects.shopping_cart_page import ShoppingCartPage
from pageobjects.checkout_your_info_page import CheckoutYourInformationPage
from pageobjects.checkout_overview_page import CheckoutOverviewPage
from pageobjects.checkout_complete_page import CheckoutCompletePage

@when('the user clicks the shopping cart link')
def click_cart_link(context):
    context.products_page.click_shopping_cart_link()

@then('the user should see the shopping cart page with "{item_name}"')
def verify_cart_page(context, item_name):
    context.shopping_cart_page.verify_on_cart_page()
    items_in_cart = context.shopping_cart_page.get_cart_items_details()
    found_item = False
    for item in items_in_cart:
        if item["name"] == item_name:
            found_item = True
            break
    assert found_item, f"Item '{item_name}' not found in cart."


@when('the user clicks the checkout button')
def click_checkout_button(context):
    context.shopping_cart_page.click_checkout()

@then('the user should see the checkout information page')
def verify_checkout_info_page(context):
    context.checkout_info_page.verify_on_checkout_info_page()


@when('the user enters checkout information "{first_name}", "{last_name}", "{postal_code}"')
def enter_checkout_info(context, first_name, last_name, postal_code):
    first_name_val = "" if first_name == "<BLANK>" else first_name
    last_name_val = "" if last_name == "<BLANK>" else last_name
    postal_code_val = "" if postal_code == "<BLANK>" else postal_code
    context.checkout_info_page.enter_checkout_information(first_name, last_name, postal_code)

@when('the user clicks the continue button')
def click_continue_button(context):
    context.checkout_info_page.click_continue()

@then('the user should see the checkout overview page')
def verify_checkout_overview_page(context):
    context.checkout_overview_page.verify_on_checkout_overview_page()

@then('the user should see "{item_name}" in the order summary')
def verify_item_in_order_summary(context, item_name):
    assert context.checkout_overview_page.verify_item_in_overview(item_name), \
        f"Item '{item_name}' not found in checkout overview summary."


@when('the user clicks the finish button')
def click_finish_button(context):
    context.checkout_overview_page.click_finish()

@then('the user should see the checkout complete page')
def verify_checkout_complete_page(context):
    context.checkout_complete_page.verify_on_checkout_complete_page()

@then('the user should see a "{message}" message')
def verify_thank_you_message(context, message):
    actual_message = context.checkout_complete_page.get_thank_you_message()
    assert actual_message == message, \
        f"Expected thank you message '{message}' but got '{actual_message}'."

@then('the user should see an error message "{error_message}"')
def verify_error_message(context, error_message):
    actual_error = context.checkout_info_page.get_error_message()
    assert actual_error == error_message, \
        f"Expected error message '{error_message}' but got '{actual_error}'."