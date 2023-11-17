from playwright.sync_api import Page, expect


def test_logout(page: Page) -> None:
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_text("Login").click()

    burger_menu_icon = page.locator("button#react-burger-menu-btn")
    burger_menu_icon.click()
    logout_link = page.locator("a#logout_sidebar_link")
    logout_link.click()

    login_button = page.locator("input#login-button")
    expect(login_button).to_contain_text("Login")
