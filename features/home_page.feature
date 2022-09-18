Feature: I will test 3 different links on the home page of the http://automationpractice.com/ website
  Scenario: I will test the Contact Us link on the Home Page of the automationpractice.com website
    Given Home Page: I am on the home page of the website
    When Home Page: I click the Contact Us button
    Then Home Page: I verify if the Contact Us link is correct


  Scenario: I will test the Sign In link on the Home Page of the automationpractice.com website
    Given Home Page: I am on the home page of the website
    When Home Page: I click the Sign In button
    Then Home Page: I verify if the Sign In link is correct


  Scenario: I will test the Newsletter link on the Home Page of the automationpractice.com website
    Given Home Page: I am on the home page of the website
    When Home Page: I input a new "dorelbobita19@gmail.com" address and press enter
    Then Home Page: I verify that I receive the subscribed success message
