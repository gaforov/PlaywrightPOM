class CheckoutPage:
    def __init__(self, page):
        self.page = page
        self._first_name = page.locator("#first-name")
        self._last_name = page.locator("#last-name")
        self._zip_code = page.locator("#postal-code")
        self._continue_button = page.locator("#continue")
        self._finish_button = page.locator("button#finish")
        self._order_confirmation_message = page.locator("//h2[@class='complete-header']")

    def enter_first_name(self, first_name):
        return self._first_name.fill(first_name)

    def enter_last_name(self, last_name):
        return self._last_name.fill(last_name)

    def enter_zip_code(self, zip_code):
        return self._zip_code.fill(zip_code)

    def enter_checkout_details(self, first_name, last_name, zip_code):
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_zip_code(zip_code)
        return self

    def click_continue_button(self):
        return self._continue_button.click()

    def click_finish_button(self):
        return self._finish_button.click()

    def get_order_confirmation_message(self):
        return self._order_confirmation_message
