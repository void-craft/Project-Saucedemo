from selenium.webdriver.common.by import By
from .base_page import BasePage
from selenium import webdriver


class LoginPage(BasePage):
    URL = 'https://www.saucedemo.com/'
    HOME_URL = 'https://www.saucedemo.com/inventory.html'

    LOCKEDOUT_USERNAME = 'locked_out_user'
    VALID_PASSWORD = 'secret_sauce'

    EXPECTED_ERROR_MESSAGE = 'Epic sadface: Username and password do not match any user in this service'

    USERNAME_FIELD = (By.ID, 'user-name')
    PASSWORD_FIELD = (By.ID, 'password')
    LOGIN_BUTTON = (By.ID, 'login-button')
    ERROR_MESSAGE_LABEL = (By.XPATH, "//h3[@data-test='error']")

    def enter_username(self, username):
        self.clear_and_send_keys(self.USERNAME_FIELD, username)

    def enter_password(self, password):
        self.clear_and_send_keys(self.PASSWORD_FIELD, password)

    def click_login_button(self):
        self.wait_for_element(self.LOGIN_BUTTON).click()

    def get_error_message(self):
        message = self.wait_for_element(self.ERROR_MESSAGE_LABEL)
        message = message.text
        return message
