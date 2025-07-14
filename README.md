# Project-SauceDemo: Selenium BDD Test Automation Framework

This project is a comprehensive Selenium test automation framework built using the **Behave BDD (Behavior-Driven Development)** framework and the **Page Object Model (POM)** design pattern. It automates functional tests for the SauceDemo e-commerce website, ensuring key functionalities work as expected and identifying any defects.

The framework is designed for **readability, maintainability, and scalability**, following industry best practices for robust test automation.

## Key Technologies Used

* **Python:** The primary programming language.
* **Selenium WebDriver:** For browser automation and interaction with web elements.
* **Behave:** A popular BDD framework for Python, allowing tests to be written in a human-readable Gherkin syntax (Given, When, Then).
* **Allure Behave:** Integration for generating rich, interactive test reports with detailed steps, screenshots, and execution trends.
* **WebDriver Manager:** Automatically handles downloading and managing browser drivers (e.g., ChromeDriver), eliminating manual setup.

## Framework Design Principles

* **Behavior-Driven Development (BDD):** Test scenarios are defined in `.feature` files using Gherkin, making them understandable by both technical and non-technical stakeholders.
* **Page Object Model (POM):** Separates UI element locators and interactions from test logic, improving code reusability and maintainability.
* **Modular and Layered Structure:** Clear separation of concerns (features, step definitions, page objects, utilities, environment hooks).
* **Robust Element Interactions:** Implements "safe interaction" methods in the BasePage to automatically handle and retry actions that might be interrupted by unexpected browser-level popups (like password managers).

## Features Automated

This project automates the following key functionalities of the SauceDemo website:

1.  **User Login:**
    * Successful login with standard credentials.
    * Handling of "locked out" user scenarios.
    * Verification of "performance glitch" user behavior (slow loading).
    * Verification of "problem user" behavior (broken images).
2.  **Product Management:**
    * Adding items to the shopping cart from the products page.
    * Removing items from the shopping cart.

## Project Structure
```
Project-SauceDemo/
├── features/                 # Contains .feature files (Gherkin scenarios)
│   ├── login.feature
│   ├── add_to_cart.feature
│   ├── remove_from_cart.feature
│   ├── environment.py        # Behave hooks for browser setup/teardown and global configurations
│   └── steps/                # Python step definition files
│       ├── common_steps.py
│       ├── login_steps.py
│       ├── add_to_cart_steps.py
│       └── remove_from_cart_steps.py
├── pageobjects/              # Page Object Model classes
│   ├── base_page.py          # Base class for common WebDriver interactions
│   ├── home_page.py
│   ├── login_page.py
│   └── products_page.py
├── utils/                    # Utility functions (e.g., config readers, helper functions - if any are added later)
├── allure_reports/           # Directory for generated Allure test reports (raw data)
├── venv/                     # Python virtual environment (ignored by Git)
├── .gitignore                # Specifies files/directories to be ignored by Git
├── requirements.txt          # Lists all Python dependencies
└── README.md                 # Project documentation
```

## Setup Instructions

To set up and run this project locally:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/Project-SauceDemo.git](https://github.com/your-username/Project-SauceDemo.git)
    cd Project-SauceDemo
    ```

2.  **Create and activate a Python virtual environment:**
    ```bash
    python -m venv venv
    # On Windows:
    .\venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Install Allure Commandline (if you want to generate HTML reports):**
    Allure Commandline is a separate tool required to convert the raw Allure results into interactive HTML reports.
    * **macOS (Homebrew):**
        ```bash
        brew install allure
        ```
    * **Windows (Scoop - recommended):**
        ```bash
        scoop install allure
        ```
        *(If you don't have Scoop, install it first: `iex (new-object net.webclient).downloadstring('https://get.scoop.sh')`)*
    * **Linux (apt-based):**
        ```bash
        sudo apt-add-repository ppa:qameta/allure && sudo apt-get update && sudo apt-get install allure-commandline
        ```
    * **Other/Manual:** Download from [Allure GitHub releases](https://github.com/allure-framework/allure2/releases) and add its `bin` directory to your system's PATH.

## How to Run Tests

Ensure your virtual environment is activated before running any commands.

### Run All Tests

To execute all feature files and see the console output:

```bash
behave --no-capture
(The --no-capture flag prevents Behave from capturing stdout/stderr of steps, allowing you to see print() statements in real-time.)
```

### Run Specific Features or Scenarios
#### Run a specific feature file:

```Bash
behave features/login.feature
```

#### Run a specific scenario (by line number):

```Bash
behave features/add_to_cart.feature:4
```

#### Run scenarios by tag (if defined in your feature files, e.g., @smoke):

```Bash
behave -t smoke
```

## Generate Allure Reports
Generate raw Allure results: This command runs all tests and saves the detailed results in the allure_reports/ directory.

```Bash
behave -f allure_behave.formatter:AllureFormatter -o allure_reports/ ./features/
```
(It's good practice to clear previous results before generating new ones: rm -rf allure_reports/* on macOS/Linux or Remove-Item -Recurse -Force allure_reports\* on Windows PowerShell.)

#### Serve the HTML report
This command builds the interactive HTML report and opens it in your default web browser.

```Bash
allure serve allure_reports/
```

## Troubleshooting Common Issues
#### SessionNotCreatedException (Chrome/ChromeDriver version mismatch):
This framework uses Selenium 4.11.2+'s built-in driver management (Service()). Ensure your selenium package is up-to-date (pip install --upgrade selenium). If the issue persists, your Chrome browser version might be exceptionally new (e.g., Canary build) and may require using a stable Chrome release.

#### Unexpected Browser Popups (e.g., Password Manager):
The framework includes extensive ChromeOptions and "safe interaction" methods in BasePage to automatically dismiss these. If they still interfere:

Ensure features/environment.py has all the recommended prefs and add_argument options.

If the popup has a specific "OK" or "Cancel" button, verify the POPUP_DISMISS_BUTTON locator in pageobjects/base_page.py is accurate.

As a last resort, consider running tests in headless mode (options.add_argument('--headless=new') in environment.py) or using a clean, un-synced Chrome user profile to avoid personalized browser notifications.

#### TimeoutException (Element not found):

Incorrect Locator: Double-check the locator (e.g., By.ID, By.CSS_SELECTOR, By.XPATH) in the relevant Page Object class.

Insufficient Wait Time: Adjust the timeout argument in self.wait_for_element() or self.wait_for_element_to_be_clickable() in BasePage.

Page State/Navigation: Ensure the application is actually reaching the expected page state before the element is looked for.

AttributeError / NameError:
These are Python coding errors. Double-check method names, variable names, and ensure all necessary import statements are present at the top of your .py files.