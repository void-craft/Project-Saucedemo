# features/checkout.feature
@checkout
Feature: Saucedemo Checkout Process
  As a logged-in user with items in my cart,
  I want to successfully complete an order,
  And also handle invalid checkout information.

  Background: User is logged in and has items in cart
    Given the user is on the saucedemo website
    And the user enters the password
    When the user enters the username "standard_user"
    And the user clicks the login button
    Then the user should see the products page
    When the user adds the items to the cart                 
    Then the user should see the total number of cart items  
    When the user clicks the shopping cart link
    Then the user should see the shopping cart page with "Sauce Labs Backpack"

  @valid_checkout
  Scenario: Successful checkout with valid information
    When the user clicks the checkout button
    Then the user should see the checkout information page
    When the user enters checkout information "John", "Doe", "12345"
    And the user clicks the continue button
    Then the user should see the checkout overview page
    And the user should see "Sauce Labs Backpack" in the order summary
    When the user clicks the finish button
    Then the user should see the checkout complete page
    And the user should see a "Thank you for your order!" message

  @invalid_checkout
  Scenario Outline: Checkout with invalid or missing information
    When the user clicks the checkout button
    Then the user should see the checkout information page
    When the user enters checkout information "<firstName>", "<lastName>", "<postalCode>"
    And the user clicks the continue button
    Then the user should see an error message "<errorMessage>"

    Examples:
      | firstName | lastName | postalCode | errorMessage                 |
      | <BLANK>   | Doe      | 12345      | Error: First Name is required|
      | John      | <BLANK>  | 12345      | Error: Last Name is required |
      | John      | Doe      | <BLANK>    | Error: Postal Code is required |
      | <BLANK>   | <BLANK>  | <BLANK>    | Error: First Name is required|