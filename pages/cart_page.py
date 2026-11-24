from playwright.sync_api import Page, expect, Locator

class CartPage:

    CART_URL = "https://www.saucedemo.com/cart.html"
    INVENTORY_URL = "https://www.saucedemo.com/inventory.html"

    def __init__(self, page: Page): 
        self.page = page

        self.title = page.locator('[data-test="title"]')
        self.cart_container = page.locator(".cart_list")

        self.cart_items = page.locator(".cart_item") #product card
        self.product_names = page.locator('[data-test="inventory-item-name"]')
        self.product_prices = page.locator('[data-test="inventory-item-price"]')
        self.product_quantities = page.locator('[data-test="item-quantity"]')
        self.continue_shopping_button = page.locator('[data-test="continue-shopping"]')
        self.cart_badge = page.locator('[data-test="shopping-cart-badge"]')

    def wait_until_loaded(self) -> None:
        expect(self.page).to_have_url(self.CART_URL)
        expect(self.title).to_have_text("Your Cart")
        expect(self.cart_container).to_be_visible()

    # scopes the Remove button to its corresponding product
    def get_cart_item(self, product_name: str, ) -> Locator:
        # Use get_by_text(..., exact=True) instead of has_text to prevent partial substring matches/needing to use regex.
        item = self.cart_items.filter(has=self.page.get_by_text(product_name, exact=True,))
        # prevent strict mode errors, catch duplicates since locators are lazy.
        expect(item, f"Expected one cart item for '{product_name}'", ).to_have_count(1)
        return item

    def get_product_names(self) -> list[str]:
        return self.product_names.all_inner_texts()

    def get_product_prices(self) -> list[float]:
        prices = self.product_prices.all_inner_texts()
        return [float(price.replace("$", "")) for price in prices]

    def get_product_quantity(self, product_name: str, ) -> int:
        item = self.get_cart_item(product_name)
        quantity = item.locator('[data-test="item-quantity"]').inner_text()
        return int(quantity)

    def remove_product(self, product_name: str, ) -> None:
        item = self.get_cart_item(product_name)
        remove_button = item.get_by_role("button", name="Remove", )
        remove_button.click()
        expect(item, f"Product '{product_name}' should be removed", ).to_have_count(0)

    def assert_cart_items(self, expected_products: list[dict], ) -> None:
        expect(self.cart_items, "Unexpected number of products in cart", ).to_have_count(len(expected_products))

        for product in expected_products:
            item = self.get_cart_item(product["name"])
            expect(item.locator('[data-test="inventory-item-name"]')).to_have_text(product["name"])
            expect(item.locator('[data-test="inventory-item-price"]')).to_have_text(f"${product['price']:.2f}")
            expect(item.locator('[data-test="item-quantity"]')).to_have_text("1")

    def assert_empty_cart(self) -> None:
        expect(self.cart_items,"Cart should contain no products",).to_have_count(0)
        expect(self.cart_badge,"Cart badge should disappear when cart is empty",).to_have_count(0)

    def open_inventory(self) -> None:
        self.continue_shopping_button.click()
        expect(self.page).to_have_url(self.INVENTORY_URL)