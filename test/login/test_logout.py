from playwright.sync_api import Page, expect

from src.pages.LoginPage import LoginPage


def test_logout(setup_teardown) -> None:
    page = setup_teardown
    credentials = {'username': 'standard_user', 'password': 'secret_sauce'}
    login_page = LoginPage(page)
    products_list_page = login_page.login(credentials)
    products_list_page.logout()
    expect(login_page.login_button).to_contain_text("Login")
    # OR
    # expect(login_page.login_button).to_be_visible()

