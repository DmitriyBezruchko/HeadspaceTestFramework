'''
This modile containts shared fixtures
'''

import json
import pytest
import selenium.webdriver
from selenium.webdriver.chrome.service import Service



@pytest.fixture
def config(scope='session'):
    with open('config.json') as config_file:
        config = json.load(config_file)

    assert config['browser'] in ['Firefox', 'Chrome', 'Headless Chrome']
    assert isinstance(config['implicit_wait'], int)
    assert config['implicit_wait'] > 0

    # Return config so it can be used
    return config


@pytest.mark.parametrize("x", ["selenium.webdriver.Safari()", "selenium.webdriver.Chrome()"])
@pytest.fixture
def driver_setup(config):
    #Initialize the WebDriver instance
    if config['browser'] == 'Firefox':
        driver = selenium.webdriver.Firefox()
    elif config['browser'] == 'Chrome':
        service = Service(executable_path="/Users/dmytro/Programming/drivers/chromedriver")
        driver = selenium.webdriver.Chrome(service=service)
    elif config['browser'] == 'Headless Chrome':
        opts = selenium.webdriver.ChromeOptions()
        opts.add_argument('headless')
        driver = selenium.webdriver.Chrome(options=opts)
    else:
        raise Exception(f'Browser "{config["browser"]}" is not supported')

    #Make its calls wait up to 10 seconds for elements to appear
    #driver = x
    driver.implicitly_wait(config['implicit_wait'])

    # Return the WebDriver instance for the setup
    yield driver

    # Quit the WebDriver instance for the cleanup
    driver.quit()
