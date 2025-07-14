# features/environment.py
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import TimeoutException

from pageobjects.login_page import LoginPage
from pageobjects.products_page import ProductsPage
from pageobjects.base_page import BasePage

def before_all(context):
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging', 'enable-automation'])

    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "safeBrowse.enabled": True,
        "safeBrowse.malware.enabled": False,
        "profile.default_content_setting_values.notifications": 2,
        "profile.password_manager_leak_detection": False
    }
    
    options.add_experimental_option("prefs", prefs)

    service = Service()
    context.driver = webdriver.Chrome(service=service, options=options)
    context.driver.implicitly_wait(10)

    context.login_page = LoginPage(context.driver)
    context.products_page = ProductsPage(context.driver)
    context.base_page = BasePage(context.driver)
    context.base_url = context.login_page.URL 

def before_scenario(context, scenario):
    context.driver.delete_all_cookies()
    context.driver.get(context.base_url)
    context.driver.maximize_window()

def after_scenario(context, scenario):
    if scenario.status == 'failed':
        scenario_name = scenario.name.replace(" ", "_").replace("/", "_")
        screenshot_dir = "allure_reports/screenshots" 
        os.makedirs(screenshot_dir, exist_ok=True)
        screenshot_path = os.path.join(screenshot_dir, f"{scenario_name}.png")
        try:
            context.driver.save_screenshot(screenshot_path)
            print(f"Screenshot saved to: {screenshot_path}")
        except Exception as e:
            print(f"Could not save screenshot: {e}")

def after_all(context):
    if hasattr(context, 'driver') and context.driver:
        context.driver.quit()