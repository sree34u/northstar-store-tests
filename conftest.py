import os

import pytest
from dotenv import load_dotenv
from playwright.sync_api import Page, expect

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.product_details_page import ProductDetails

load_dotenv()
SAUCE_USERNAME = os.getenv("SAUCE_USERNAME")
SAUCE_PASSWORD = os.getenv("SAUCE_PASSWORD")

if not SAUCE_USERNAME or not SAUCE_PASSWORD:
    raise RuntimeError("SAUCE_USERNAME and SAUCE_PASSWORD must be set")

expect.set_options(timeout=6_000)

@pytest.fixture
def login_page(page: Page) -> LoginPage:
    return LoginPage(page)

@pytest.fixture
def inventory_page(page: Page) -> InventoryPage:
    login = LoginPage(page)

    login.open()
    login.login(SAUCE_USERNAME, SAUCE_PASSWORD)

    inventory = InventoryPage(page)
    inventory.wait_until_loaded()
    return inventory

@pytest.fixture
def product_details_page(page: Page) -> ProductDetails:
    return ProductDetails(page)