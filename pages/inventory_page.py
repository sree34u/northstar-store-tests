from playwright.sync_api import Page, Locator, expect


class InventoryPage:
    INVENTORY_URL = "https://www.saucedemo.com/inventory.html"

    def __init__(self, page: Page):
        self.page = page

        # Page-level elements
        self.title = page.locator('[data-test="title"]')
        self.inventory_container = page.locator("#inventory_container")

        # Product collection
        self.product_items = page.locator(
            ".inventory_item"
        )

        self.product_names = page.locator(
            '[data-test="inventory-item-name"]'
        )

        self.product_images = page.locator(
            "img.inventory_item_img"
        )

        self.product_descriptions = page.locator(
            '[data-test="inventory-item-desc"]'
        )

        self.product_prices = page.locator(
            '[data-test="inventory-item-price"]'
        )

        # Shopping cart
        self.cart_link = page.locator(
            '[data-test="shopping-cart-link"]'
        )

        self.cart_badge = page.locator(
            '[data-test="shopping-cart-badge"]'
        )

        # Sorting
        self.sort_dropdown = page.locator(
            '[data-test="product-sort-container"]'
        )

    def wait_until_loaded(self) -> None:
        expect(
            self.page,
            "Inventory page URL was not loaded",
        ).to_have_url(self.INVENTORY_URL)

        expect(
            self.title,
            "Inventory page title is incorrect",
        ).to_have_text("Products")

        expect(
            self.product_items.first,
            "No product card became visible",
        ).to_be_visible()

    def get_product(self, product_name: str) -> Locator:
        product = self.product_items.filter(
            has=self.page.get_by_text(
                product_name,
                exact=True,
            )
        )

        expect(
            product,
            f"Expected exactly one product card for '{product_name}'",
        ).to_have_count(1)

        return product

    def get_product_names(self) -> list[str]:
        return self.product_names.all_inner_texts()

    def get_product_prices(self) -> list[float]:
        prices = self.product_prices.all_inner_texts()

        return [
            float(price.replace("$", ""))
            for price in prices
        ]

    def get_product_price(self, product_name: str) -> float:
        product = self.get_product(product_name)

        price = product.locator(
            '[data-test="inventory-item-price"]'
        ).inner_text()

        return float(price.replace("$", ""))

    def get_product_description(self, product_name: str) -> str:
        product = self.get_product(product_name)

        return product.locator(
            '[data-test="inventory-item-desc"]'
        ).inner_text()

    def get_product_image(self, product_name: str) -> Locator:
        product = self.get_product(product_name)

        return product.locator(
            "img.inventory_item_img"
        )

    def get_add_to_cart_button(
        self,
        product_name: str,
    ) -> Locator:
        product = self.get_product(product_name)

        return product.locator(".btn_inventory")

    def add_product_to_cart(
        self,
        product_name: str,
    ) -> None:
        self.get_add_to_cart_button(product_name).click()

    def add_products_to_cart(
        self,
        product_names: list[str],
    ) -> None:
        for product_name in product_names:
            self.add_product_to_cart(product_name)

    def assert_product_count(
        self,
        expected_count: int,
    ) -> None:
        expect(
            self.product_items,
            "Unexpected number of products displayed",
        ).to_have_count(expected_count)

    def assert_product_card(
        self,
        product_name: str,
        expected_price: float,
    ) -> None:
        product = self.get_product(product_name)

        expect(
            product,
            f"Product card for '{product_name}' is not visible",
        ).to_be_visible()

        expect(
            product.locator(
                '[data-test="inventory-item-name"]'
            ),
            f"Product name is incorrect for '{product_name}'",
        ).to_have_text(product_name)

        expect(
            product.locator(
                '[data-test="inventory-item-desc"]'
            ),
            f"Product description is not visible for '{product_name}'",
        ).to_be_visible()

        expect(
            product.locator("img.inventory_item_img"),
            f"Product image is not visible for '{product_name}'",
        ).to_be_visible()

        expect(
            product.locator(
                '[data-test="inventory-item-price"]'
            ),
            f"Product price is incorrect for '{product_name}'",
        ).to_have_text(f"${expected_price:.2f}")

        expect(
            product.locator(".btn_inventory"),
            f"Add to cart button is not visible for '{product_name}'",
        ).to_be_visible()

    def assert_cart_count(
        self,
        expected_count: int,
    ) -> None:
        if expected_count == 0:
            expect(
                self.cart_badge,
                "Cart badge should not be visible when cart is empty",
            ).not_to_be_visible()
            return

        expect(
            self.cart_badge,
            f"Expected cart count to be {expected_count}",
        ).to_have_text(str(expected_count))

    def sort_products(self, option: str) -> None:
        self.sort_dropdown.select_option(option)

    def open_product(self, product_name: str) -> None:
        self.get_product(product_name).locator(
            '[data-test="inventory-item-name"]'
        ).click()

    def open_cart(self) -> None:
        self.cart_link.click()