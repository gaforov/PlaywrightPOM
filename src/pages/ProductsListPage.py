class ProductsListPage:
    def __init__(self, page):
        self.page = page
        self._products_header = page.locator("span.title")

    @property
    def product_header(self):
        return self._products_header
