from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class HeadspaceLoginPage:

    URL = 'https://www.headspace.com/login'

    # Locators

    EMAIL_FIELD = (By.ID, 'email')
    PASSWORD_FIELD = (By.ID, 'password')
    LOGIN_BUTTON = (By.XPATH, '//button[@data-testid="submit-login-btn"]')
    WRONG_PASSWORD_VALIDATION_MESSAGE = (By.XPATH, "//p[@data-testid='error-message']")
    WRONG_EMAIL_VALIDATION_MESSAGE = (By.XPATH, "//p[@data-testid='username-error-message']")
    SIGNUP_LINK = (By.LINK_TEXT, 'Sign up for free')
    FORGOT_PASSWORD_LINK = (By.XPATH, '//a[@data-testid="forgot-password"]')

    # Test Data

    PROPER_USER_EMAIL = 'bezruchko.dmitriy@gmail.com'
    WRONG_USER_EMAIL = 'bezruchko'
    PROPER_USER_PASSWORD = 's589160589160'
    WRONG_USER_PASSWORD = '12345678'

    def __init__(self, driver):
        self.driver = driver

    def open_main_url(self):
        self.driver.get(self.URL)

    def do_login(self, user_email, password):
        self.driver.find_element(*self.EMAIL_FIELD).send_keys(user_email)
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def click_signup_link(self):
        self.driver.find_element(*self.SIGNUP_LINK).click()

    def click_forgot_password_link(self):
        self.driver.find_element(self.FORGOT_PASSWORD_LINK).click()

    def get_wrong_password_error_message(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.WRONG_PASSWORD_VALIDATION_MESSAGE))
        message = self.driver.find_element(*self.WRONG_PASSWORD_VALIDATION_MESSAGE).text
        return message

    def get_wrong_email_error_message(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.WRONG_EMAIL_VALIDATION_MESSAGE))
        message = self.driver.find_element(*self.WRONG_EMAIL_VALIDATION_MESSAGE).text
        return message
