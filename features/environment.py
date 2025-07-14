# features/environment.py
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import TimeoutException, WebDriverException # Import WebDriverException for general driver errors

from pageobjects.login_page import LoginPage
from pageobjects.products_page import ProductsPage
from pageobjects.base_page import BasePage

from pageobjects.shopping_cart_page import ShoppingCartPage
from pageobjects.checkout_your_info_page import CheckoutYourInfoPage
from pageobjects.checkout_overview_page import CheckoutOverviewPage
from pageobjects.checkout_complete_page import CheckoutCompletePage

def before_all(context):
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging', 'enable-automation'])

    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "safeBrowse.enabled": True,
        "safeBrowse.malware.enabled": False,
        "profile.default_content_setting_values.notifications": 2,
        "profile.managed_default_content_settings.images": 1,
        "profile.password_manager_leak_detection": False
    }
    
    options.add_experimental_option("prefs", prefs)

    options.add_argument("--disable-features=EnableEphemeralBadges,PasswordSuggestion,AutofillServerPredictions")
    options.add_argument("--password-manager-testing")
    options.add_argument("--no-default-browser-check")
    options.add_argument("--no-first-run")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-translate")
    options.add_argument("--disable-save-password-bubble")
    options.add_argument("--disable-notifications")
    
    service = Service()
    context.driver = webdriver.Chrome(service=service, options=options)
    context.driver.implicitly_wait(10)

    # Initialize all page objects in before_all so they are available in context
    context.login_page = LoginPage(context.driver)
    context.products_page = ProductsPage(context.driver)
    context.base_page = BasePage(context.driver)
    context.base_url = context.login_page.URL 

    context.shopping_cart_page = ShoppingCartPage(context.driver)
    context.checkout_info_page = CheckoutYourInfoPage(context.driver)
    context.checkout_overview_page = CheckoutOverviewPage(context.driver)
    context.checkout_complete_page = CheckoutCompletePage(context.driver)

def before_scenario(context, scenario):
    context.driver.get(context.base_url)
    context.driver.maximize_window()
    context.driver.delete_all_cookies() 
    context.driver.execute_script("window.localStorage.clear();")
    context.driver.execute_script("window.sessionStorage.clear();")

def after_scenario(context, scenario):
    try:
        if hasattr(context, 'driver') and context.driver.session_id:
            if context.driver.current_url != context.base_url + "inventory.html":
                context.driver.get(context.base_url + "inventory.html")
                context.products_page.wait_for_element(context.products_page.SPAN_TITLE_CSS, timeout=10)

            context.products_page.remove_all_items_from_cart() 
            print("Cart successfully cleared in after_scenario.")

    except (WebDriverException, Exception) as e:
        print(f"WARNING: Failed to clear cart in after_scenario: {e}")

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