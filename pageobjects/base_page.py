from selenium.common import NoSuchElementException, TimeoutException, ElementClickInterceptedException
from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select
import random
import string


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(self.driver)
        self.wait = WebDriverWait(self.driver, 10)

    def open_url(self, url):
        self.driver.get(url)

    def wait_3_seconds(self, locator, timeout=3):
        wait = WebDriverWait(self.driver, timeout)
        element = wait.until(ec.visibility_of_element_located(locator))
        return element

    def wait_for_element(self, locator, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        element = wait.until(ec.visibility_of_element_located(locator))
        return element

    def switch_to_frame(self, frame_locator):
        """Switches to the frame with the specified locator"""
        frame_element = self.wait_for_element(frame_locator)
        self.driver.switch_to.frame(frame_element)

    def switch_to_default_content(self):
        """Switches back to the default content"""
        self.driver.switch_to.default_content()

    def click_element(self, locator):
        element = self.wait_for_element(locator)
        element.click()

    def get_text(self, locator):
        element = self.wait_for_element(locator)
        return element.text

    def get_title(self):
        return self.driver.title

    def get_current_url(self):
        return self.driver.current_url

    def get_page_source(self):
        return self.driver.page_source

    def get_element_attribute(self, locator, attribute_name):
        element = self.wait_for_element(locator)
        return element.get_attribute(attribute_name)

    def is_element_visible(self, locator):
        try:
            element = self.driver.find_element(*locator)
            return element.is_displayed()
        except NoSuchElementException:
            return False

    def is_element_present(self, locator):
        try:
            self.driver.find_element(*locator)
            return True
        except NoSuchElementException:
            return False

    def send_keys(self, locator, text):
        element = self.wait_for_element(locator)
        element.send_keys(text)

    def clear_and_send_keys(self, by_locator, text):
        element = self.wait_for_element(by_locator)
        element.clear()
        element.send_keys(text)

    def press_enter(self, locator):
        element = self.wait_for_element(locator)
        element.send_keys(Keys.RETURN)

    def press_tab(self, locator):
        element = self.wait_for_element(locator)
        element.send_keys(Keys.TAB)

    def press_control(self, locator, key):
        element = self.wait_for_element(locator)
        element.send_keys(Keys.CONTROL, key)

    def press_escape(self, locator):
        element = self.wait_for_element(locator)
        element.send_keys(Keys.ESCAPE)

    def wait_for_elements(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(ec.presence_of_all_elements_located(locator))

    def wait_for_element_to_be_clickable(self, locator, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        element = wait.until(ec.element_to_be_clickable(locator))
        return element

    def select_dropdown_by_visible_text(self, locator, text):
        element = self.wait_for_element(locator)
        select = Select(element)
        select.select_by_visible_text(text)

    def select_dropdown_by_value(self, locator, value):
        element = self.wait_for_element(locator)
        select = Select(element)
        select.select_by_value(value)

    def select_dropdown_by_index(self, locator, index):
        element = self.wait_for_element(locator)
        select = Select(element)
        select.select_by_index(index)

    def select_radio_button_by_value(self, locator, value):
        elements = self.wait_for_elements(locator)
        for element in elements:
            if element.get_attribute('value') == value:
                element.click()
                break

    def select_checkbox(self, locator):
        element = self.wait_for_element(locator)
        if not element.is_selected():
            element.click()

    def deselect_checkbox(self, locator):
        element = self.wait_for_element(locator)
        if element.is_selected():
            element.click()

    def upload_file(self, locator, file_path):
        element = self.wait_for_element(locator)
        element.send_keys(file_path)

    def clear_text(self, locator):
        element = self.wait_for_element(locator)
        element.clear()

    def submit_form(self, locator):
        element = self.wait_for_element(locator)
        element.submit()

    def is_element_enabled(self, locator):
        element = self.wait_for_element(locator)
        return element.is_enabled()

    def is_element_selected(self, locator):
        element = self.wait_for_element(locator)
        return element.is_selected()

    def is_element_displayed(self, locator):
        element = self.wait_for_element(locator)
        return element.is_displayed()

    def scroll_to_element(self, locator):
        element = self.wait_for_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def click_element_with_javascript(self, locator):
        element = self.wait_for_element(locator)
        self.driver.execute_script("arguments[0].click();", element)

    def create_hover_action(self, locator):
        element = self.wait_for_element(locator)
        actions = ActionChains(self.driver)
        return actions.move_to_element(element)

    def hover_over_element(self, locator):
        hover = self.create_hover_action(locator)
        hover.perform()

    def hover_over_element_and_click(self, locator):
        hover = self.create_hover_action(locator)
        hover.click.perform()

    def hover_over_element_and_right_click(self, locator):
        hover = self.create_hover_action(locator)
        hover.context_click.perform()

    def hover_over_element_and_double_click(self, locator):
        hover = self.create_hover_action(locator)
        hover.double_click.perform()

    @staticmethod
    def generate_random_email(length=10):
        email = ''.join(random.choices(string.ascii_lowercase + string.digits, k=length)) + "@example.com"
        return email

    @staticmethod
    def generate_random_password(length):
        password = ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
        return password

    def go_back(self):
        self.driver.back()

    def maximize_window(self):
        self.driver.maximize_window()

    def double_click_element(self, locator):
        element = self.wait_for_element(locator)
        self.actions.double_click(element).perform()

    def context_click_element(self, locator):
        element = self.wait_for_element(locator)
        self.actions.context_click(element).perform()

    def click_and_hold_element(self, locator):
        element = self.wait_for_element(locator)
        self.actions.click_and_hold(element).perform()

    def drag_and_drop(self, source_locator, target_locator):
        source_element = self.wait_for_element(source_locator)
        target_element = self.wait_for_element(target_locator)
        self.actions.drag_and_drop(source_element, target_element).perform()

    def drag_and_drop_by_offset(self, locator, x_offset, y_offset):
        element = self.wait_for_element(locator)
        self.actions.drag_and_drop_by_offset(element, x_offset, y_offset).perform()

    def release_element(self):
        self.actions.release().perform()

    def key_down(self, key):
        self.actions.key_down(key).perform()

    def key_up(self, key):
        self.actions.key_up(key).perform()

    def move_by_offset(self, x_offset, y_offset):
        self.actions.move_by_offset(x_offset, y_offset).perform()

    def move_to_element_with_offset(self, locator, x_offset, y_offset):
        element = self.wait_for_element(locator)
        self.actions.move_to_element_with_offset(element, x_offset, y_offset).perform()

    def move_to_new_tab(self):
        self.actions.key_down(Keys.CONTROL).send_keys(Keys.TAB).key_up(Keys.CONTROL).perform()

    def move_to_previous_tab(self):
        self.actions.key_down(Keys.CONTROL).key_down(Keys.SHIFT).send_keys(Keys.TAB).key_up(Keys.SHIFT).key_up(
            Keys.CONTROL).perform()

    def zoom_in(self):
        self.actions.key_down(Keys.CONTROL).send_keys(Keys.ADD).key_up(Keys.CONTROL).perform()

    def zoom_out(self):
        self.actions.key_down(Keys.CONTROL).send_keys(Keys.SUBTRACT).key_up(Keys.CONTROL).perform()

    def scroll_down(self):
        self.actions.send_keys(Keys.PAGE_DOWN).perform()

    def scroll_up(self):
        self.actions.send_keys(Keys.PAGE_UP).perform()
