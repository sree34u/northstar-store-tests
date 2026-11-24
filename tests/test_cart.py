import pytest

from pages.cart_page import CartPage
from test_data.products import PRODUCTS

def get_products(product_names: list[str]) -> list[dict]:

    products_by_name = {
        product["name"]: product
        for product in PRODUCTS
    }

    return [
        products_by_name[name]
        for name in product_names
    ]

def get_products(product_names: list[str]) -> list[dict]:

    return [product for product in PRODUCTS if product["name"] in product_names]

def test_added_product_appears_in_cart(inventory_page):

    product_name = "Sauce Labs Backpack"

    inventory_page.add_product_to_cart(product_name)

    inventory_page.open_cart()

    cart = CartPage(inventory_page.page)
    cart.wait_until_loaded()

    expected_products = get_products([product_name])

    cart.assert_cart_items(expected_products)

def test_multiple_products_appear_in_cart(inventory_page):

    product_names = [
        "Sauce Labs Backpack",
        "Sauce Labs Bike Light",
    ]

    inventory_page.add_products_to_cart(product_names)

    inventory_page.open_cart()

    cart = CartPage(inventory_page.page)
    cart.wait_until_loaded()

    expected_products = get_products(product_names)

    cart.assert_cart_items(expected_products)


def test_cart_product_names_match_expected_data(inventory_page):

    product_names = [
        "Sauce Labs Backpack",
        "Sauce Labs Bike Light",
    ]

    inventory_page.add_products_to_cart(product_names)

    inventory_page.open_cart()

    cart = CartPage(inventory_page.page)
    cart.wait_until_loaded()

    actual_names = sorted(cart.get_product_names())

    expected_names = sorted(product_names)

    assert actual_names == expected_names


def test_cart_product_prices_match_expected_data(inventory_page):

    product_names = [
        "Sauce Labs Backpack",
        "Sauce Labs Bike Light",
    ]

    inventory_page.add_products_to_cart(product_names)

    inventory_page.open_cart()

    cart = CartPage(inventory_page.page)
    cart.wait_until_loaded()

    actual_prices = sorted(cart.get_product_prices())

    expected_prices = sorted(
        product["price"]
        for product in get_products(product_names)
    )

    assert actual_prices == expected_prices


def test_cart_product_quantities_are_correct(inventory_page):

    product_names = [
        "Sauce Labs Backpack",
        "Sauce Labs Bike Light",
    ]

    inventory_page.add_products_to_cart(product_names)

    inventory_page.open_cart()

    cart = CartPage(inventory_page.page)
    cart.wait_until_loaded()

    for product_name in product_names:

        actual_quantity = cart.get_product_quantity(
            product_name
        )

        assert actual_quantity == 1


def test_user_can_remove_individual_product(inventory_page):

    product_names = [
        "Sauce Labs Backpack",
        "Sauce Labs Bike Light",
    ]

    inventory_page.add_products_to_cart(product_names)

    inventory_page.open_cart()

    cart = CartPage(inventory_page.page)
    cart.wait_until_loaded()

    cart.remove_product("Sauce Labs Backpack")

    assert cart.get_product_names() == [
        "Sauce Labs Bike Light"
    ]

    cart.assert_cart_items(
        get_products(["Sauce Labs Bike Light"])
    )


def test_cart_displays_empty_state_after_removing_all_products(
    inventory_page,
):

    product_names = [
        "Sauce Labs Backpack",
        "Sauce Labs Bike Light",
    ]

    inventory_page.add_products_to_cart(product_names)

    inventory_page.open_cart()

    cart = CartPage(inventory_page.page)
    cart.wait_until_loaded()

    for product_name in product_names:
        cart.remove_product(product_name)

    cart.assert_empty_cart()


def test_user_can_navigate_from_inventory_to_cart(inventory_page):

    inventory_page.open_cart()

    cart = CartPage(inventory_page.page)

    cart.wait_until_loaded()


def test_user_can_navigate_from_cart_to_inventory(inventory_page):

    inventory_page.open_cart()

    cart = CartPage(inventory_page.page)
    cart.wait_until_loaded()

    cart.open_inventory()

    inventory_page.wait_until_loaded()


def test_cart_contents_persist_during_navigation(inventory_page):

    product_names = [
        "Sauce Labs Backpack",
        "Sauce Labs Bike Light",
    ]

    inventory_page.add_products_to_cart(product_names)

    inventory_page.open_cart()

    cart = CartPage(inventory_page.page)
    cart.wait_until_loaded()

    cart.assert_cart_items(
        get_products(product_names)
    )

    cart.open_inventory()

    inventory_page.wait_until_loaded()

    inventory_page.assert_cart_count(2)

    inventory_page.open_cart()

    cart.wait_until_loaded()

    cart.assert_cart_items(
        get_products(product_names)
    )