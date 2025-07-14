# Project-SauceDemo: Selenium BDD Automation Framework

This project is a comprehensive Selenium test automation framework utilizing **Behave BDD** and the **Page Object Model (POM)**. It automates functional tests for the SauceDemo e-commerce website, ensuring key functionalities work as expected and identifying any defects.

The framework is designed for **readability, maintainability, and scalability**, following industry best practices for robust test automation.

## Key Technologies

* **Python:** The primary programming language.
* **Selenium WebDriver:** Browser automation.
* **Behave:** BDD framework (Gherkin syntax).
* **Allure Behave:** Rich test reporting.
* **WebDriver Manager:** Automated driver management.

## Framework Principles

* **Behavior-Driven Development (BDD):** Human-readable test scenarios.
* **Page Object Model (POM):** Separates UI interaction from test logic.
* **Modular Design:** Clear separation of features, steps, and pages.
* **Robustness:** Includes "safe interaction" methods to handle unexpected browser popups.

## Features Automated

1.  **User Login:** Successful, locked out, performance glitch, problem user scenarios.
2.  **Product Management:** Adding and removing items from the cart.
3.  **Checkout Process:** Successful checkout and invalid/missing information handling.

## Project Structure
```
Project-SauceDemo/
├── features/                 # Gherkin .feature files & Behave hooks (environment.py)
│   └── steps/                # Python step definitions
├── pageobjects/              # Page Object Model classes (BasePage, LoginPage, ProductsPage, Checkout pages)
├── allure_reports/           # Generated Allure raw test data
├── venv/                     # Python virtual environment (ignored by Git)
├── .gitignore                # Git ignored files
└── requirements.txt          # Project dependencies
```

## Setup & Run

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/Project-SauceDemo.git](https://github.com/your-username/Project-SauceDemo.git)
    cd Project-SauceDemo
    ```
2.  **Setup Virtual Environment & Install Dependencies:**
    ```bash
    python -m venv venv
    # On Windows: .\venv\Scripts\activate
    # On macOS/Linux: source venv/bin/activate
    pip install -r requirements.txt
    ```
3.  **Install Allure Commandline (for HTML reports):**
    * `brew install allure` (macOS)
    * `scoop install allure` (Windows)
    * `sudo apt-get install allure-commandline` (Linux)

### Run Tests

* **All Tests:**
    ```bash
    behave --no-capture
    ```
* **Specific Scenario (by tag):**
    ```bash
    behave -t successful_checkout
    ```
    *(Use `-t tag1 -t tag2` for AND logic, `-t tag1,tag2` for OR logic, `-t ~tag` to exclude.)*

### Generate & View Reports

```bash
rm -rf allure_reports/* # (Optional: clear old reports)
behave -f allure_behave.formatter:AllureFormatter -o allure_reports/ ./features/
allure serve allure_reports/
```
### Troubleshooting
SessionNotCreatedException (ChromeDriver): Ensure selenium is updated (pip install --upgrade selenium).

Browser Popups: Framework uses ChromeOptions and BasePage "safe actions" to dismiss.

TimeoutException (Element not found): Verify locators in Page Objects and ensure sufficient wait times.

AttributeError / NameError: Check Python imports and method/variable names for typos.

Cart State Not Clean: before_scenario clears localStorage, sessionStorage, and cookies to ensure a fresh cart state.