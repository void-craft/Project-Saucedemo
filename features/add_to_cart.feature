Feature: Saucedemo Add to cart
  As a user, I want to add items to the cart from the products page.

  Scenario: the user adds the items to the cart
    Given the user is on the saucedemo website
    And the user enters the password
    When the user enters the username "standard_user"
    And the user clicks the login button
    Then the user should see the products page
    When the user adds the items to the cart
    Then the user should see the total number of cart items