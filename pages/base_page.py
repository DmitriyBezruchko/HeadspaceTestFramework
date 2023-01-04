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

    def click(self, webelement):
        element = self.wait.until(expected_conditions.element_to_be_clickable(webelement))
        element.click()

     def fill_text(self, webelement, txt):
         element = self.wait.until(expected_conditions.element_to_be_clickable(webelement))
         element.clear()
         element.send_keys(txt)

    def clear_text(self, webelement):
        element = self.wait.until(expected_conditions.element_to_be_clickable(webelement))
        element.clear()

    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def get_text(self, webelement):
        element = self.wait.until(expected_conditions.visibility_of_element_located(webelement))
        return element.text

    def is_element_displayed(self, webelement):
        try:
            return webelement.is_displayed()
        except StaleElementRefernceException:
            return False
        except NoSuchElementException:
            return False


    def navigate_to(self, url):
        self.driver.get(url)

    def get_element(self, locator):
        element = self.driver.find_element(locator)

        return element


