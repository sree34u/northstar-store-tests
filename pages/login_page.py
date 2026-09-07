from playwright.sync_api import Page, expect

class LoginPage:
    def __init__(self, page: Page):
        self.page = page

        self.username_input = page.locator("[data-test='username']")
        self.password_input = page.locator("#password")
        self.login_button = page.get_by_role("button", name="Login")
        self.error_message = page.locator("[data-test='error']")

    def open(self) -> None:
        self.page.goto("https://www.saucedemo.com/")

    def login(self, username: str, password: str) -> None:
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def expect_login_error(self, message: str) -> None:
        expect(self.error_message).to_contain_text(message)