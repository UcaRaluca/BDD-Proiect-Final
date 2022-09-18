from behave import *

@when('Search Page: I input a "{product}" name in the search bar')
def step_impl(context, product):
    context.search_page_object.search_product(product)

@when('Search Page: I click search button')
def step_impl(context):
    context.search_page_object.click_search_button()

@when('Search Page: I choose a product from the returned list')
def step_impl(context):
    context.search_page_object.choose_product_from_list()

@when('Search Page: I click the Add to cart button')
def step_impl(context):
    context.search_page_object.add_to_cart()

@then('Search Page: The product is added to the cart and I can choose the Continue shopping option')
def step_impl(context):
    context.search_page_object.choose_continue()

@when('Search Page: I click the cart button')
def step_impl(context):
    context.search_page_object.click_cart_button()

@then('Search Page: I verify that I have a product in my cart')
def step_impl(context):
    context.search_page_object.verify_cart()

@when('Search Page: I delete the product')
def step_impl(context):
    context.search_page_object.delete_cart_product()

@then('Search Page: I verify that I receive the message cart is empty.')
def step_impl(context):
    context.search_page_object.verify_empty_cart()

