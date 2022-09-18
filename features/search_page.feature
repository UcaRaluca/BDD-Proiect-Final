Feature: I will verify the search product option, add to cart and empty cart on automationpractice.com website.

  Scenario: I am on Home page, search for a product in the search bar, choose a product from the returned list,
             add it to cart and choose the continue shopping option.
    Given Home Page: I am on the home page of the website
    When Search Page: I input a "dress" name in the search bar
    When Search Page: I click search button
    When Search Page: I choose a product from the returned list
    When Search Page: I click the Add to cart button
    Then Search Page: The product is added to the cart and I can choose the Continue shopping option


  Scenario: I check the cart if the product is present, delete it, and than verify if I receive the message cart is empty.
    Given Home Page: I am on the home page of the website
    When Search Page: I click the cart button
    Then Search Page: I verify that I have a product in my cart
    When Search Page: I delete the product
    Then Search Page: I verify that I receive the message cart is empty.