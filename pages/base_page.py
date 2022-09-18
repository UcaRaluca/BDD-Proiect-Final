from browser import Browser
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import unittest

class Base_page(Browser, unittest.TestCase):
    pass