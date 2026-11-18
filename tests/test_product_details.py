from playwright.sync_api import expect
from test_data.pytest_params import PRODUCT_TEST_CASES

@PRODUCT_TEST_CASES
def test_product_details_are_displayed(product_details_page):
    expect(product_details_page.product_name).to_be_visible()
    expect(product_details_page.product_desc).to_be_visible()
    expect(product_details_page.product_image).to_be_visible()
    expect(product_details_page.product_price).to_be_visible()

@PRODUCT_TEST_CASES
def test_product_details_match_catalogue(product, product_details_page):
    expect(product_details_page.product_name).to_have_text(product["name"])
    expect(product_details_page.product_price).to_have_text(f"${product['price']:.2f}")

@PRODUCT_TEST_CASES
def test_add_product_to_cart(product, product_details_page):
    product_details_page.add_to_cart()
    expect(product_details_page.cart_badge).to_have_text("1")

@PRODUCT_TEST_CASES
def test_remove_product_from_cart(product, product_details_page):
    product_details_page.add_to_cart()
    product_details_page.remove_cart()
    expect(product_details_page.cart_badge).to_have_count(0)

@PRODUCT_TEST_CASES
def test_return_to_products(product, product_details_page):
    product_details_page.go_back_to_products()
    expect(product_details_page.page).to_have_url(
        "https://www.saucedemo.com/inventory.html"
    )