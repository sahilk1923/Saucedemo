# conftest.py
import pytest
from utils.driver import get_driver
from pages.login_page import LoginPage

@pytest.fixture(scope="class")
def driver():
    # Initialize the WebDriver
    driver = get_driver()
    yield driver
    # Quit the WebDriver after tests
    driver.quit()

@pytest.fixture(scope="class")
def login(driver):
    # Perform login for test setup
    login_page = LoginPage(driver)
    login_page.navigate_to_login()
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()
    return driver
