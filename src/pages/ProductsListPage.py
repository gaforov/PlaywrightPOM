class ProductsListPage:
    def __init__(self, page):
        self.page = page
        self._products_header = page.locator("span.title")
        self._burger_menu_icon = page.locator("button#react-burger-menu-btn")
        self._logout_link = page.locator("a#logout_sidebar_link")

    @property
    def product_header(self):
        """This function returns locator/selector for product header text"""
        return self._products_header

    def click_burger_menu_btn(self):
        """This function will click on the Burger Menu icon from the header"""
        self._burger_menu_icon.click()

    def click_logout(self):
        """This will click the logout link"""
        self._logout_link.click()

    def logout(self):
        """Logout from the Sauce Demo page"""
        self.click_burger_menu_btn()
        self.click_logout()