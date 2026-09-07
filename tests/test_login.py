from playwright.sync_api import expect
from pages.login_page import LoginPage
import os
from dotenv import load_dotenv

load_dotenv()

SAUCE_USERNAME = os.getenv("SAUCE_USERNAME")
SAUCE_PASSWORD = os.getenv("SAUCE_PASSWORD")

def test_valid_user_can_login(page):
    login_page = LoginPage(page)

    login_page.open()
    login_page.login(SAUCE_USERNAME, SAUCE_PASSWORD)

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

def test_invalid_user_cannot_login(page):
    login_page = LoginPage(page)

    login_page.open()
    login_page.login("invalid_user", "invalid_password")

    login_page.expect_login_error("Epic sadface: Username and password do not match any user in this service")

def test_locked_out_user(page):
    login_page = LoginPage(page)

    login_page.open()
    login_page.login("locked_out_user", SAUCE_PASSWORD)

    login_page.expect_login_error("Epic sadface: Sorry, this user has been locked out.")
