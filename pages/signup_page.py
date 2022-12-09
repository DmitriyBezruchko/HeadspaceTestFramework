from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class SignUpPage:

    URL = 'https://www.headspace.com/register'

    # Locators


    # Test Data

    def __init__(self, driver):
        self.driver = driver

    def open_main_url(self):
        self.driver.get(self.URL)

