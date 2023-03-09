import pytest
from playwright.sync_api import Playwright


@pytest.fixture
def set_up(page):
    # Asses - Given
    # browser = playwright.chromium.launch(headless=False, slow_mo=500)
    # browser = playwright.chromium.launch(headless=False)
    # context = browser.new_context()
    # Open new page
    # page = context.new_page()
    page.set_default_timeout(15000)
    page.goto("https://symonstorozhenko.wixsite.com/website-1")

    yield page
