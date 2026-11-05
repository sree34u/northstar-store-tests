from playwright.sync_api import expect
from pages.login_page import LoginPage

def test_valid_user_can_login(page, login_page: LoginPage, sauce_username: str, sauce_password: str,):
    login_page = LoginPage(page)

    login_page.open()
    login_page.login(sauce_username, sauce_password)

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

def test_invalid_user_cannot_login(login_page: LoginPage,):

    login_page.open()
    login_page.login("invalid_user", "invalid_password")

    login_page.expect_login_error("Epic sadface: Username and password do not match any user in this service")

def test_locked_out_user(login_page: LoginPage, sauce_password: str,):
    login_page.open()
    login_page.login("locked_out_user", sauce_password)

    login_page.expect_login_error("Epic sadface: Sorry, this user has been locked out.")
