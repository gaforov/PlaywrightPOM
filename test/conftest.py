import playwright
import pytest


@pytest.fixture()
def setup_teardown(page) -> None:
    page.goto("https://www.saucedemo.com/")
    page.set_viewport_size({"width": 2000, "height": 1200})
    yield page
