from browser import Browser
from pages.home_page import Home_page
from pages.search_page import Search_page
from pages.sign_in_page import Sign_in_page

def before_all(context):
    context.browser = Browser()
    context.home_page_object = Home_page()
    context.search_page_object = Search_page()
    context.sign_in_page_object = Sign_in_page()


def after_all(context):
    context.browser.close()