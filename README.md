# Project-saucedemo

The Saucedemo project is a Selenium test automation project using the Behave framework to automate functional tests for the Saucedemo e-commerce website.

It includes feature files written in the Gherkin language, step definitions in Python, and page object model design pattern to interact with the website .

The project aims to ensure the functionality of the website is working as expected, and to identify and report any defects found during the testing process.

It uses allure to generate reports.

* The packages used in this framework are:
  
  1. Python
  2. Selenium
  3. behave
  4. allure-behave


* BDD behave is used to test the following features:

  1. Login
      a. Locked out feature
      b. Performance errors
      c. Glitches
      d. Error free login
  2. Adding items to cart
  3. Removing items from cart

* Commands used to run the test cases and to generate reports are:  

   a. The results are generated using allure-behave:

   behave -f allure_behave.formatter:AllureFormatter -o allure_reports/login_report ./features/login.feature
   behave -f allure_behave.formatter:AllureFormatter -o allure_reports/add_to_cart_report ./features/add_to_cart.feature
   behave -f allure_behave.formatter:AllureFormatter -o allure_reports/remove_from_cart ./features/remove_from_cart.feature


   b. Then they are converted to html files with the command:

   allure serve allure_reports/login_report
   allure serve allure_reports/add_to_cart_report
   allure serve allure_reports/remove_from_cart