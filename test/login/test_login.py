from playwright.sync_api import Page, expect

from src.pages.LoginPage import LoginPage


def test_login(setup_teardown) -> None:
    page = setup_teardown
    credentials = {'username': 'standard_user', 'password': 'secret_sauce'}
    login_page = LoginPage(page)
    products_list_page = login_page.login(credentials)

    expect(products_list_page.product_header).to_be_visible()
    expect(products_list_page.product_header).to_have_text("Products")


def test_login_invalid_user(setup_teardown) -> None:
    page = setup_teardown
    credentials = {'username': 'invalid_user', 'password': 'secret_sauce'}
    login_page = LoginPage(page)
    login_page.login(credentials)

    expected_error_message = "Epic sadface: Username and password do not match any user in this service"
    expect(login_page.error_message_locator).to_contain_text(expected_error_message)


def test_login_no_username(setup_teardown) -> None:
    page = setup_teardown
    login_page = LoginPage(page)
    login_page.enter_password('secret_sauce')
    login_page.click_login()

    expected_fail_message = "Username is required"
    expect(login_page.error_message_locator).to_contain_text(expected_fail_message)


def test_login_no_password(setup_teardown) -> None:
    page = setup_teardown
    login_page = LoginPage(page)
    login_page.enter_username("standard_user")
    login_page.click_login()

    expected_fail_message = "Password is required"
    expect(login_page.error_message_locator).to_contain_text(expected_fail_message)
