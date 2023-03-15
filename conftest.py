import pytest
from playwright.sync_api import Playwright


@pytest.fixture(scope="session")
def set_up(browser):
    # Asses - Given
    # browser = playwright.chromium.launch(headless=False, slow_mo=500)
    # browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    # Open new page
    page = context.new_page()
    page.set_default_timeout(15000)
    page.goto("https://symonstorozhenko.wixsite.com/website-1")

    yield page
    page.close()


@pytest.fixture(scope="session")
def login_set_up(set_up):
    page = set_up
    page.wait_for_load_state("networkidle")
    page.get_by_role("button", name="Log In").click()
    page.get_by_test_id("signUp.switchToSignUp").click()
    page.get_by_test_id("siteMembersDialogLayout").get_by_test_id("buttonElement").click()
    page.get_by_test_id("emailAuth").get_by_label("Email").fill("symon.storozhenko@gmail.com")
    page.get_by_label("Password").fill("test123", timeout=3000)
    page.get_by_test_id("submit").get_by_test_id("buttonElement").click()
    page.wait_for_load_state("networkidle")

    yield page


@pytest.fixture(scope="session")
def go_to_new_collection_page(set_up):
    page = set_up
    page.set_default_timeout(15000)
    page.goto("/new-collection")

    yield page
