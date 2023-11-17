from src.pages.ProductsListPage import ProductsListPage


class LoginPage:
    def __init__(self, page):
        self.page = page
        self._username = page.get_by_placeholder("Username")
        self._password = page.get_by_placeholder("Password")
        self._login_btn = page.get_by_text("Login")
        self._error_message = page.locator("div.login-box h3")

    def enter_username(self, username):
        self._username.clear()
        self._username.fill(username)

    def enter_password(self, password):
        self._password.clear()
        self._password.fill(password)

    def click_login(self):
        self._login_btn.click()

    def login(self, credentials):
        self.enter_username(credentials['username'])
        self.enter_password(credentials['password'])
        self.click_login()
        return ProductsListPage(self.page)

    @property
    def error_message_locator(self):
        return self._error_message

