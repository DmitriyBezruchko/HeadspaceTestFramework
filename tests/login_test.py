import allure
import pytest
import selenium.webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from pages.login_page import HeadspaceLoginPage
'''

'''


@allure.severity(allure.severity_level.BLOCKER)
@allure.epic("Security")
@allure.feature("Login")
@pytest.mark.security


@allure.description("Valid Login")
@allure.title("Login with valid credentials test")
def test_proper_login(driver_setup):
    login_page = HeadspaceLoginPage(driver_setup)
    login_page.open_main_url()
    login_page.do_login(HeadspaceLoginPage.PROPER_USER_EMAIL, HeadspaceLoginPage.PROPER_USER_PASSWORD)
    WebDriverWait(driver_setup, 10).until(EC.title_is('Meditate'))
    assert "Meditate" in driver_setup.title

@allure.description("Login Invalid Password")
@allure.title("Login with invalid password test")
def test_wrong_password_login(driver_setup):
    login_page = HeadspaceLoginPage(driver_setup)
    login_page.open_main_url()
    login_page.do_login(HeadspaceLoginPage.PROPER_USER_EMAIL, HeadspaceLoginPage.WRONG_USER_PASSWORD)
    login_page.get_wrong_password_error_message()

    assert "Either your email or password was incorrect. Please try again." in login_page.get_wrong_password_error_message()

@allure.description("Login Invalid Email")
@allure.title("Login with invalid email test")
def test_wrong_email_login(driver_setup):
    login_page = HeadspaceLoginPage(driver_setup)
    login_page.open_main_url()
    login_page.do_login(HeadspaceLoginPage.WRONG_USER_EMAIL, HeadspaceLoginPage.PROPER_USER_PASSWORD)
    login_page.get_wrong_email_error_message()
    assert "Please verify e-mail address is correct" in login_page.get_wrong_email_error_message()

#
# def test_signup_link_working(driver_setup):
#     login_page = HeadspaceLoginPage(driver_setup)
#     login_page.click_signup_link()
#     assert 'Register with Headspace' in driver_setup.title
#
#
# def test_forgot_password_link_working(driver_setup):
#     login_page = HeadspaceLoginPage(driver_setup)
#     login_page.click_forgot_password_link()
#     assert 'RESET MY PASSWORD' in driver_setup.find_element(By.XPATH, "//div[@data-testid='forgotten-password-email-cta']").text

