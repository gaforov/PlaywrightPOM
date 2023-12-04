from src.pages.CartPage import CartPage


class ProductsListPage:
    def __init__(self, page):
        self.page = page
        self._products_header = page.locator("span.title")
        self._burger_menu_icon = page.locator("button#react-burger-menu-btn")
        self._logout_link = page.locator("a#logout_sidebar_link")
        self._add_to_cart = page.locator("//div[text()='Sauce Labs Backpack']/ancestor::div[@class='inventory_item_description']//button")
        self._cart_icon = page.locator("a.shopping_cart_link")

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

    def get_add_or_remove_cart_locator(self, product):
        """This will return Add to cart OR Remove from the cart button"""
        return self.page.locator("//div[text()='"+product+"']/ancestor::div[@class='inventory_item_description']//button")

    def click_add_to_cart_or_remove(self, product):
        self.get_add_or_remove_cart_locator(product).click()
        return self

    def click_cart_icon(self):
        self._cart_icon.click()
        return CartPage(self.page)


