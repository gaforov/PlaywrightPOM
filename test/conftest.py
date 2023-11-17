import pytest


@pytest.fixture()
def setup_teardown(page) -> None:
    page.goto("https://www.saucedemo.com/")
    yield page
