from playwright.sync_api import expect

from src.pages.LoginPage import LoginPage


def test_add_to_cart(setup_teardown) -> None:
    page = setup_teardown
    credentials = {'username': 'standard_user', 'password': 'secret_sauce'}
    login_page = LoginPage(page)
    products_list_page = login_page.login(credentials)
    product_name = "Sauce Labs Bolt T-Shirt"
    products_list_page.click_add_to_cart_or_remove(product_name)
    expect(products_list_page.get_add_or_remove_cart_locator(product_name)).to_contain_text("Remove")


def test_remove_from_cart(setup_teardown) -> None:
    page = setup_teardown
    credentials = {'username': 'standard_user', 'password': 'secret_sauce'}
    login_page = LoginPage(page)
    products_list_page = login_page.login(credentials)
    product_name = "Sauce Labs Bolt T-Shirt"
    products_list_page.click_add_to_cart_or_remove(product_name)
    products_list_page.click_add_to_cart_or_remove(product_name)
    expect(products_list_page.get_add_or_remove_cart_locator(product_name)).to_contain_text("Add to cart")
