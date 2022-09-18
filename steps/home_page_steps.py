from behave import *

@given('Home Page: I am on the home page of the website')
def step_impl(context):
    context.home_page_object.navigate_to_home_page()

@when('Home Page: I click the Contact Us button')
def step_impl(context):
    context.home_page_object.click_contact_us()

@then('Home Page: I verify if the Contact Us link is correct')
def step_impl(context):
    context.home_page_object.verif_link_contact()

@when('Home Page: I click the Sign In button')
def step_impl(context):
    context.home_page_object.click_sign_in()

@then('Home Page: I verify if the Sign In link is correct')
def step_impl(context):
    context.home_page_object.verif_link_sign_in()

@when('Home Page: I input a new "{email}" address and press enter')
def step_impl(context, email):
    context.home_page_object.input_newsletter(email)

@then('Home Page: I verify that I receive the subscribed success message')
def step_impl(context):
    context.home_page_object.verif_mesaj_newsletter()