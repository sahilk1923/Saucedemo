# tests/test_login.py

# this test set can be expanded to verify navigating to the login scren
# then verify the availability of username, password, login button
# then verify enter input in username and password,
import pytest
from pages.login_page import LoginPage
# from utils.driver import get_driver

class TestLogin:

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.login_page = LoginPage(driver)
        
    def test_login_valid_credentials(self):
        self.login_page.navigate_to_login()
        self.login_page.enter_username("standard_user")
        self.login_page.enter_password("secret_sauce")
        self.login_page.click_login()
        assert self.login_page.is_login_successful(), "Login failed with valid credentials."

    def test_login_invalid_credentials(self):
        self.login_page.navigate_to_login()
        self.login_page.enter_username("invalid_user")
        self.login_page.enter_password("wrong_password")
        self.login_page.click_login()
        assert self.login_page.is_error_message_displayed(), "Error message not displayed for invalid credentials."
