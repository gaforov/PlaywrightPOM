from playwright.sync_api import expect

from src.pages.CheckoutPage import CheckoutPage
from src.pages.LoginPage import LoginPage


def test_place_order(setup_teardown) -> None:
    """Verify that user is able to place an order successfully"""
    page = setup_teardown
    credentials = {'username': 'standard_user', 'password': 'secret_sauce'}
    login_page = LoginPage(page)
    products_list_page = login_page.login(credentials)

    product_name = "Sauce Labs Backpack"
    (products_list_page.click_add_to_cart_or_remove(product_name)
     .click_cart_icon()
     .click_checkout_button()
     .enter_checkout_details("John", "Doe", "90143")
     .click_continue_button()
     # .click_finish_button()
     )

    checkout_page = CheckoutPage(page)
    checkout_page.click_finish_button()
    expected_order_confirmation_text = "Thank you for your order!"
    expect(checkout_page.get_order_confirmation_message()).to_have_text(expected_order_confirmation_text)
