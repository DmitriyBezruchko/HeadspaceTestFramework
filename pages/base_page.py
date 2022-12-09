from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def get_page_title(self):
        pass

    def navigate_to(self, url):
        self.driver.get(url)

    def get_element(self, locator):
        element = self.driver.find_element(locator)

        return element


