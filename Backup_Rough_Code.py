import pytest
import selenium.webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

'''
1. Open Login link https://my.asos.com/identity//login?signin
expected - page fully loaded
2. Find login field
field presented
3. Fill Login field
check filled ?
4. Find password field
field presented
5. Fill password field
check filled ?
6. Find sign in button
button presented
7. Click sign in button
succesfully signed in


def asos_login_test(driver):
    login_page = LoginPage(driver)

    login_page.load(url)
    assert title
    
    login_page.login()
    assert login is proper

    login_page.wrong_password_login()
    assert 'Looks like either your email address or password were incorrect. Wanna try again?'

    login_page.wrong_email_login()
    assert 'Email fail! Please type in your correct email address'

    Вопросы 
    сколько ставится implicit wait
    проверка после find element ?

'''

# setup

service = Service(executable_path="/Users/dmytro/Programming/drivers/chromedriver")
browser = selenium.webdriver.Chrome(service=service)

# Proper login

browser.get('https://www.headspace.com/login')
WebDriverWait(browser, 10).until(EC.title_is('Log In'))

email_field = browser.find_element(By.ID, 'email')
WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.ID, 'email')))
email_field.send_keys('bezruchko.dmitriy@gmail.com')

WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.ID, 'password')))
password_field = browser.find_element(By.ID, 'password')
password_field.send_keys('s589160589160')

log_in_button = browser.find_element(By.XPATH, '//button[@data-testid="submit-login-btn"]')
log_in_button.click()
WebDriverWait(browser, 10).until(EC.title_is('Meditate'))
assert "Meditate" in browser.title

# Proper login wrong password

browser.get('https://www.headspace.com/login')
WebDriverWait(browser, 10).until(EC.title_is('Log In'))

WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.ID, "email")))
email_field = browser.find_element(By.ID, 'email')
email_field.send_keys('bezruchko.dmitriy@gmail.com')

WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.ID, 'password')))
password_field = browser.find_element(By.ID, 'password')
password_field.send_keys('123456')

log_in_button = browser.find_element(By.XPATH, '//button[@data-testid="submit-login-btn"]')
log_in_button.click()

WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, "//p[@data-testid='error-message']")))
password_error_message = browser.find_element(By.XPATH, "//p[@data-testid='error-message']")

assert "Either your email or password was incorrect. Please try again." in password_error_message.text

# Wrong email validation message

browser.get('https://www.headspace.com/login')

WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.ID, "email")))
email_field = browser.find_element(By.ID, 'email')
email_field.send_keys('bezruchko')

log_in_button = browser.find_element(By.XPATH, '//button[@data-testid="submit-login-btn"]')
log_in_button.click()

WebDriverWait(browser, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//p[@data-testid='username-error-message']")))
email_error_message = browser.find_element(By.XPATH, "//p[@data-testid='username-error-message']")

assert "Please verify e-mail address is correct" in email_error_message.text

# Sign up link is working

browser.get('https://www.headspace.com/login')
sign_up_link = browser.find_element(By.LINK_TEXT, 'Sign up for free')
sign_up_link.click()
WebDriverWait(browser, 10).until(EC.title_is('Register with Headspace'))
assert 'Register with Headspace' in browser.title

# Forgot Password link is working

browser.get('https://www.headspace.com/login')
forgot_password_link = browser.find_element(By.XPATH, '//a[@data-testid="forgot-password"]')
forgot_password_link.click()
WebDriverWait(browser, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//div[@data-testid='forgotten-password-email-cta']")))
reset_password_button = browser.find_element(By.XPATH, "//div[@data-testid='forgotten-password-email-cta']")
assert 'RESET MY PASSWORD' in reset_password_button.text




