Feature: Saucedemo Remove from cart
  As a user, I want to remove all the items from the cart from the products page.

  Scenario: the user removes items from the cart
    Given the user is on the saucedemo website
    And the user enters the password
    When the user enters the username "standard_user"
    And the user clicks the login button
    Then the user should see the products page
    And the user should see the total number of cart items
    When the user removes the items from the cart
    Then the user should not see the counter
