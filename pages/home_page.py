from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.base_page import Base_page
from time import sleep

class Home_page(Base_page):
    CONTACT_US_BUTTON = (By.XPATH, '//a[text()="Contact us"]')
    SIGN_IN_BUTTON = (By.XPATH, '//a[@class="login"]')
    NEWSLETTER_INPUT = (By.ID, 'newsletter-input')
    SUCCESS_MESSAGE = (By.XPATH, '//p[contains(text(),"Newsletter : You have successfully subscribed to this newsletter.")]')


    def navigate_to_home_page(self):
        self.chrome.get('http://automationpractice.com/index.php')

    def click_contact_us(self):
        self.chrome.find_element(*self.CONTACT_US_BUTTON).click()

    def verif_link_contact(self):
        actual_link = self.chrome.current_url
        expected_link = 'http://automationpractice.com/index.php?controller=contact'
        self.assertEqual(actual_link, expected_link, f'{actual_link} is not the expected one')

    def click_sign_in(self):
        self.chrome.find_element(*self.SIGN_IN_BUTTON).click()

    def verif_link_sign_in(self):
        actual_link = self.chrome.current_url
        self.assertTrue(
            actual_link == 'http://automationpractice.com/index.php?controller=authentication&back=my-account',
            f'{actual_link} is not the expected one')

    def input_newsletter(self, email):
        input_email = self.chrome.find_element(*self.NEWSLETTER_INPUT)
        input_email.send_keys(email)  # foloseste email ca parametru si schimba adresa
        input_email.send_keys(Keys.ENTER)

    def verif_mesaj_newsletter(self):
        mesaj_succes = WebDriverWait(self.chrome, 10).until(EC.presence_of_element_located(self.SUCCESS_MESSAGE))
        self.assertTrue(mesaj_succes.is_displayed(), f' {mesaj_succes} nu e vizibil')

