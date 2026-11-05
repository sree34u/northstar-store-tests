from playwright.sync_api import Locator, Page, expect

class ProductDetails:
    def __init__(self, page: Page):
        self.page = page

        self.product_name = page.locator('[data-test="inventory-item-name"]')
        self.product_desc = page.locator('[data-test="inventory-item-desc"]')
        self.product_image = page.locator(".inventory_details_img")
        self.product_price = page.locator('[data-test="inventory-item-price"]')
        self.add_to_cart_button = page.locator('[data-test="add-to-cart"]')
        self.remove_cart_button = page.locator('[data-test="remove"]')
        self.cart_badge = page.locator('[data-test="shopping-cart-badge"]')
        self.back_to_products = page.locator('[data-test="back-to-products"]')

    def wait_until_loaded(self) -> None:
        expect(self.product_name).to_be_visible()
        expect(self.product_desc).to_be_visible()
        expect(self.product_image).to_be_visible()
        expect(self.product_price).to_be_visible()

    def get_product_name(self) -> str:
        return self.product_name.inner_text()

    def get_product_desc(self) -> str:
        return self.product_desc.inner_text()

    def get_product_price(self) -> float:
        price = self.product_price.inner_text()
        return float(price.replace("$", ""))

    def add_to_cart(self) -> None:
        self.add_to_cart_button.click()

    def remove_cart(self) -> None:
        self.remove_cart_button.click()

    def get_cart_count(self) -> int:
        if self.cart_badge.count() == 0:
            return 0
        return int(self.cart_badge.inner_text())

    def go_back_to_products(self) -> None:
        self.back_to_products.click()
