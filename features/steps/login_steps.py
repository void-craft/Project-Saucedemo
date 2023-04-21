from behave import *
from selenium import webdriver


@when('the user enters the locked out username')
def enter_username(context):
    context.login_page.enter_username(context.login_page.LOCKEDOUT_USERNAME)


@then('the user should see an error message')
def step_impl(context):
    try:
        context.actual_error_message = context.login_page.get_error_message()
    except:
        print("The user is not locked out.")
        assert False
    if context.actual_error_message == context.login_page.EXPECTED_ERROR_MESSAGE:
        print("The user is locked out")
        assert True


@when('the user enters the username "{username}"')
def step_impl(context, username):
    context.login_page.enter_username(username)
