from playwright.sync_api import expect

from src.pages.LoginPage import LoginPage


def test_place_order(setup_teardown) -> None:
    """Verify that user is able to place an order successfully"""
    page = setup_teardown
    credentials = {'username': 'standard_user', 'password': 'secret_sauce'}
    login_page = LoginPage(page)
    products_list_page = login_page.login(credentials)
    product_name = "Sauce Labs Backpack"
    products_list_page.click_add_to_cart_or_remove(product_name)