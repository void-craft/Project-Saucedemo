# features/steps/common_steps.py
import time
from behave import *
from selenium.common.exceptions import TimeoutException
from pageobjects.login_page import LoginPage
from pageobjects.products_page import ProductsPage
from pageobjects.base_page import BasePage


@given('the user is on the saucedemo website')
def open_website(context):
    pass

@given('the user enters the password')
def enter_password(context):
    context.login_page.enter_password(context.login_page.VALID_PASSWORD)


@when('the user clicks the login button')
def press_login(context):
    context.login_page.click_login_button()

@when('the user dismisses the password change popup if present')
def step_impl(context):
    try:
        ok_button = context.driver.find_element(By.XPATH, "//button[text()='OK']")
        ok_button.click()
        print("Closed 'Change Password' popup.")
    except NoSuchElementException:
        pass

@then('the user should see the products page')
def verify_products_page(context):
    context.products_page = ProductsPage(context.driver)
    context.base_page = BasePage(context.driver)
    try:
        context.base_page.wait_for_element(context.products_page.SPAN_TITLE_CSS, timeout=2)
        image_tags = context.base_page.wait_for_element(context.products_page.IMAGE_PRODUCTS_TAG)
        source_value = set(context.tag.get_attribute("source") for context.tag in image_tags)
        if len(source_value) == 1:
            print("The user is logged in and faces glitches.")
            assert True
        else:
            print("The user has logged in successfully with no issues.")
            assert True
    except:
        try:
            context.base_page.wait_for_element(context.products_page.SPAN_TITLE_CSS, timeout=6)
            print("The user is logged in and faces performance issues")
            assert True
        except:
            print("The user is unable to login")
            assert False


@then('the user closes the browser')
def close_browser(context):
    pass
