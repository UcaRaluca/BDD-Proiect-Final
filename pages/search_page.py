from selenium.webdriver.common.by import By
from pages.base_page import Base_page
from time import sleep

class Search_page(Base_page):
    SEARCH_TEXT_BOX = (By.ID, 'search_query_top')
    SEARCH_BUTTON = (By.XPATH, '//button[@name="submit_search"]')
    SEARCH_RESULTS = (By.XPATH, '//ul[@class="product_list grid row"]')
    ADD_TO_CART = (By.XPATH, '//span[text()="Add to cart"]')
    CONTINUE_SHOPPING_BUTTON = (By.XPATH, '//span[@title="Continue shopping"]')
    CART = (By.XPATH, '//a[@title="View my shopping cart"]')
    MESSAGE_CART_FULL = (By.XPATH, '//span[contains(text(), "Your shopping cart contains:")]')
    DELETE_CART = (By.XPATH, '//i[@class="icon-trash"]')
    MESSAGE_CART_EMPTY = (By.XPATH, '//p[contains(text(),"Your shopping cart is empty.")]')

    def search_product(self, product):
        self.chrome.find_element(*self.SEARCH_TEXT_BOX).send_keys(product)
        sleep(1)

    def click_search_button(self):
        self.chrome.find_element(*self.SEARCH_BUTTON).click()
        sleep(3)

    def choose_product_from_list(self):
        lista = self.chrome.find_elements(*self.SEARCH_RESULTS)
        lista[0].click()
        sleep(10)

    def add_to_cart(self):
        self.chrome.switch_to.frame(self.chrome.find_element(By.XPATH, '//iframe[@class="fancybox-iframe"]'))
        sleep(5)
        prod1 = self.chrome.find_element(*self.ADD_TO_CART)
        prod1.click()
        sleep(10)

    def choose_continue(self):
        self.chrome.find_element(*self.CONTINUE_SHOPPING_BUTTON).click()
        sleep(3)

    def click_cart_button(self):
        self.chrome.find_element(*self.CART).click()
        sleep(7)

    def verify_cart(self):
        produs_in_cos = self.chrome.find_element(*self.MESSAGE_CART_FULL)
        self.assertTrue(produs_in_cos.is_displayed(), 'Nu exista produse in cos')

    def delete_cart_product(self):
        self.chrome.find_element(*self.DELETE_CART).click()
        sleep(10)

    def verify_empty_cart(self):
        niciun_produs_in_cos = self.chrome.find_element(*self.MESSAGE_CART_EMPTY)
        self.assertTrue(niciun_produs_in_cos.is_displayed(), 'Inca sunt produse in cos')