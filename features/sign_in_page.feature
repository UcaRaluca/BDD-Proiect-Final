Feature: I will try 2 different situations on the Sign In page of automationpractice.com website
          create new account and get the error message if I try to use an email address already used.
  Scenario: From the Home Page I will click Sign In and than create an account with a new email address, verify if the
              opened page is the correct one, input details for the required fields, click Register and verify if I
              receive the success message.
    Given Home Page: I am on the home page of the website
    When Home Page: I click the Sign In button
    When Sign In Page: I input a new email "abramburica18@gmail.com"
    When Sign In Page: I click create account button
    Then Sign In Page: I verify that the opened page is the correct one
    When Sign In Page: I input the title Mrs
    When Sign In Page: I input the first name "Abram"
    When Sign In Page: I input the last name "Burica"
    When Sign In Page: I input the password "qazwsxedc"
    When Sign In Page: I input the address "Main Street 5"
    When Sign In Page: I input the city
    When Sign In Page: I choose the state
    When Sign In Page: I input the postal code "15975"
    When Sign In Page: I input the mobile number "+500229957"
    When Sign In Page: I click the Register button
    Then Sign In Page: I receive the Welcome to your account message


  Scenario:  From the Home Page I will click Sign In and than create an account with the same email address used in the
              previous scenario, than check the I receive an error message
    Given Home Page: I am on the home page of the website
    When Sign In Page: I sign out
    When Home Page: I click the Sign In button
    When Sign In Page: I input the email "abramburica18@gmail.com" used before
    When Sign In Page: I click create account button
    Then Sign In Page: I verify that I receive an error message




