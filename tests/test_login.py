import time

import pytest
from tests.pages.login_page import LoginPage


@pytest.mark.usefixtures("browser")
class TestLogin:
    base_url = "https://practicetestautomation.com/practice-test-login/"  # demo site

    def test_successful_login(self, browser):
        login_page = LoginPage(browser)
        login_page.open(self.base_url)
        login_page.enter_username("student")
        login_page.enter_password("Password123")
        login_page.click_login()
        print(login_page.get_success_message())
        assert "Congratulations" in login_page.get_success_message()

    def test_failed_login_invalid_username(self, browser):
        login_page = LoginPage(browser)
        login_page.open(self.base_url)
        login_page.enter_username("incorrectUser")
        login_page.enter_password("Password123")
        login_page.click_login()
        time.sleep(1)
        assert "Your username is invalid!" in login_page.get_error_message()

    def test_failed_login_invalid_password(self, browser):
        login_page = LoginPage(browser)
        login_page.open(self.base_url)
        login_page.enter_username("student")
        login_page.enter_password("incorrectPassword")
        login_page.click_login()
        time.sleep(1)
        assert "Your password is invalid!" in login_page.get_error_message()

    def test_empty_credentials(self, browser):
        login_page = LoginPage(browser)
        login_page.open(self.base_url)
        login_page.enter_username("")
        login_page.enter_password("")
        login_page.click_login()
        time.sleep(1)
        assert "Your username is invalid!" in login_page.get_error_message()