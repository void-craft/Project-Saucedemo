Feature: Saucedemo Login
  As a user, I want to login to the saucedemo website to see the products page.

  Background: common steps
    Given the user is on the saucedemo website
    And the user enters the password

  Scenario: Login with locked out credentials
    When the user enters the locked out username
    And the user clicks the login button
    Then the user should see an error message
    And the user closes the browser

  Scenario Outline: Login with different users
    When the user enters the username "<username>"
    And the user clicks the login button
    Then the user should see the products page
    And the user closes the browser

    Examples:
      | username                |
      | standard_user           |
      | performance_glitch_user |
      | problem_user            |
