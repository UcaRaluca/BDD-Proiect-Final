from behave import *

@when('Sign In Page: I input a new email "{email}"')
def step_impl(context, email):
    context.sign_in_page_object.input_email(email)

@when('Sign In Page: I click create account button')
def step_impl(context):
    context.sign_in_page_object.click_create_button()

@then('Sign In Page: I verify that the opened page is the correct one')
def step_impl(context):
    context.sign_in_page_object.verify_create_page()

@when('Sign In Page: I input the title Mrs')
def step_impl(context):
    context.sign_in_page_object.click_title()

@when('Sign In Page: I input the first name "{first_name}"')
def step_impl(context, first_name):
    context.sign_in_page_object.input_first_name(first_name)

@when('Sign In Page: I input the last name "{last_name}"')
def step_impl(context, last_name):
    context.sign_in_page_object.input_last_name(last_name)

@when('Sign In Page: I input the password "{password}"')
def step_impl(context, password):
    context.sign_in_page_object.input_password(password)

@when('Sign In Page: I input the address "{address}"')
def step_impl(context, address):
    context.sign_in_page_object.input_address(address)

@when('Sign In Page: I input the city')
def step_impl(context):
    context.sign_in_page_object.input_city()

@when('Sign In Page: I choose the state')
def step_impl(context):
    context.sign_in_page_object.input_state()

@when('Sign In Page: I input the postal code "{postal_code}"')
def step_impl(context, postal_code):
    context.sign_in_page_object.input_postal_code(postal_code)

@when('Sign In Page: I input the mobile number "{mobile_phone}"')
def step_impl(context, mobile_phone):
    context.sign_in_page_object.input_mobile_phone(mobile_phone)

@when('Sign In Page: I click the Register button')
def step_impl(context):
    context.sign_in_page_object.click_register()

@when('Sign In Page: I sign out')
def step_impl(context):
    context.sign_in_page_object.click_sign_out()

@when('Sign In Page: I input the email "{email}" used before')
def step_impl(context, email):
    context.sign_in_page_object.input_email(email)

@then('Sign In Page: I receive the Welcome to your account message')
def step_impl(context):
    context.sign_in_page_object.verify_success_message()

@then('Sign In Page: I verify that I receive an error message')
def step_impl(context):
    context.sign_in_page_object.verify_error_message()

