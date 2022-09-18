from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.base_page import Base_page
from time import sleep

class Sign_in_page(Base_page):
    EMAIL_CREATE_ACCOUNT = (By.XPATH, '//input[@name="email_create"]')
    CREATE_ACCOUNT_BUTTON = (By.XPATH, '//button[@id="SubmitCreate"]')
    TITLE_MRS = (By.XPATH, '//input[@id="id_gender2"]')
    FIRST_NAME = (By.ID, 'customer_firstname')
    LAST_NAME = (By.ID, 'customer_lastname')
    PASSWORD = (By.ID, 'passwd')
    ADDRESS_ADDRESS = (By.ID, 'address1')
    ADDRESS_CITY = (By.ID, 'city')  # Texas
    ADDRESS_STATE = (By.XPATH, '//option[text()="Texas"]')
    ADDRESS_ZIP_CODE = (By.ID, 'postcode')
    MOBILE_PHONE = (By.ID, 'phone_mobile')
    REGISTER_BUTTON = (By.XPATH, '//span[text()="Register"]')
    WELCOME_MESSAGE = (
    By.XPATH, '//p[text()="Welcome to your account. Here you can manage all of your personal information and orders."]')
    ERROR_MESSAGE = (By.XPATH, '//li[contains(text(),"An account using this email address ")]')
    SIGN_OUT_BUTTON=(By.XPATH, '//a[@class="logout"]')

    def input_email(self, email):
        self.chrome.find_element(*self.EMAIL_CREATE_ACCOUNT).send_keys(email)
        sleep(4)

    def click_create_button(self):
        self.chrome.find_element(*self.CREATE_ACCOUNT_BUTTON).click()
        sleep(8)

    def verify_create_page(self):
        actual_link = self.chrome.current_url
        self.assertTrue(
            actual_link == 'http://automationpractice.com/index.php?controller=authentication&back=my-account#account-creation',
            f'{actual_link} is not the expected one')


    def click_title(self):
        self.chrome.find_element(*self.TITLE_MRS).click()
        sleep(1)

    def input_first_name(self, first_name):
        self.chrome.find_element(*self.FIRST_NAME).send_keys(first_name)
        sleep(1)

    def input_last_name(self, last_name):
        self.chrome.find_element(*self.LAST_NAME).send_keys(last_name)
        sleep(1)

    def input_password(self, password):
        self.chrome.find_element(*self.PASSWORD).send_keys(password)
        sleep(1)

    def input_address(self, address):
        self.chrome.find_element(*self.ADDRESS_ADDRESS).send_keys(address)
        sleep(1)

    def input_city(self):
        self.chrome.find_element(*self.ADDRESS_CITY).send_keys('Texas')
        sleep(1)

    def input_state(self):
        self.chrome.find_element(*self.ADDRESS_STATE).click()
        sleep(1)

    def input_postal_code(self, postal_code):
        self.chrome.find_element(*self.ADDRESS_ZIP_CODE).send_keys(postal_code)
        sleep(1)

    def input_mobile_phone(self, mobile_phone):
        self.chrome.find_element(*self.MOBILE_PHONE).send_keys(mobile_phone)
        sleep(1)

    def click_register(self):
        self.chrome.find_element(*self.REGISTER_BUTTON).click()
        sleep(10)

    def click_sign_out(self):
        self.chrome.find_element(*self.SIGN_OUT_BUTTON).click()
        sleep(10)

    def verify_success_message(self):
        welcome_message = WebDriverWait(self.chrome, 10).until(EC.presence_of_element_located(self.WELCOME_MESSAGE))
        self.assertTrue(welcome_message.is_displayed(), f' {welcome_message} nu e vizibil')

    def verify_error_message(self):
        error_message = WebDriverWait(self.chrome, 10).until(EC.visibility_of_element_located(self.ERROR_MESSAGE))
        self.assertTrue(error_message.is_displayed(), f' {error_message} nu e vizibil')