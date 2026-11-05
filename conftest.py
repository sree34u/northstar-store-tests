import os

import pytest
from dotenv import load_dotenv
from playwright.sync_api import Page, expect

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.product_details_page import ProductDetails

load_dotenv()

expect.set_options(timeout=6_000)

@pytest.fixture
def sauce_username() -> str:
    username = os.getenv("SAUCE_USERNAME")

    if not username:
        pytest.fail("SAUCE_USERNAME is missing. Check your .env file.")

    return username


@pytest.fixture
def sauce_password() -> str:
    password = os.getenv("SAUCE_PASSWORD")

    if not password:
        pytest.fail("SAUCE_PASSWORD is missing. Check your .env file.")

    return password

@pytest.fixture
def login_page(page: Page) -> LoginPage:
    return LoginPage(page)

@pytest.fixture
def inventory_page(page: Page,  sauce_username: str, sauce_password: str, ) -> InventoryPage:
    
    login = LoginPage(page)

    login.open()
    login.login(sauce_username, sauce_password)

    inventory = InventoryPage(page)
    inventory.wait_until_loaded()

    return inventory

@pytest.fixture
def product_details_page(inventory_page: InventoryPage) -> ProductDetails:
    inventory_page.open_product("Sauce Labs Backpack")
    
    product_details = ProductDetails(inventory_page.page)
    product_details.wait_until_loaded() 
    
    return product_details