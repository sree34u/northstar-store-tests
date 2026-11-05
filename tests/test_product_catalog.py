import pytest

from test_data.products import (PRODUCTS, EXPECTED_PRODUCT_COUNT,SORTING_TEST_DATA,)

def test_product_catalog_is_loaded(inventory_page):
    inventory_page.assert_product_count(EXPECTED_PRODUCT_COUNT)

    for product in PRODUCTS:
        inventory_page.assert_product_card(
            product["name"],
            product["price"],
        )

def test_product_names_match_expected_data(inventory_page):
    actual_names = inventory_page.get_product_names()

    expected_names = [
        product["name"] for product in PRODUCTS
    ]

    assert actual_names == expected_names

def test_product_prices_match_expected_data(inventory_page):
    actual_prices = inventory_page.get_product_prices()

    expected_prices = [
        product["price"] for product in PRODUCTS
    ]

    assert actual_prices == expected_prices

def test_individual_product_price_matches_expected_data(inventory_page,):
    for product in PRODUCTS:
        actual_price = inventory_page.get_product_price(product["name"])

        assert actual_price == product["price"], (
            f"Unexpected price for '{product['name']}'."
            f"Expected ${product['price']:.2f},"
            f"but found ${actual_price:.2f}."
        )

def test_user_can_add_one_product_to_cart(inventory_page, ):
    inventory_page.add_product_to_cart("Sauce Labs Backpack")
    inventory_page.assert_cart_count(1)

def test_user_can_add_multiple_products_to_cart(inventory_page, ):
    products_to_add = [
        "Sauce Labs Backpack",
        "Sauce Labs Bike Light",
    ]

    inventory_page.add_products_to_cart(products_to_add)

    inventory_page.assert_cart_count(2)

def test_user_can_add_all_products_to_cart(inventory_page, ):
    product_names = [
        product["name"] for product in PRODUCTS
    ]
    inventory_page.add_products_to_cart(product_names)
    inventory_page.assert_cart_count(EXPECTED_PRODUCT_COUNT)

@pytest.mark.parametrize("sort_option, expected_order", SORTING_TEST_DATA, )
def test_products_can_be_sorted(inventory_page, sort_option, expected_order, ):
    inventory_page.sort_products(sort_option)

    actual_order = inventory_page.get_product_names()

    assert actual_order == expected_order,(
        f"Unexpected product order for '{sort_option}'."
        f"Expected: '{expected_order}'."
        f"Actual: '{actual_order}'."
    )
