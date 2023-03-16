import os
import pytest
from playwright.sync_api import expect

# PASSWORD = os.environ['PASSWORD']

try:
    PASSWORD = os.environ['PASSWORD']
except KeyError:
    import utils.secret_config
    PASSWORD = utils.secret_config.PASSWORD


@pytest.fixture()
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
    page.close()


@pytest.fixture(scope="session")
def context_creation(playwright):
    browser = playwright.chromium.launch(headless=True, slow_mo=300)
    context = browser.new_context()
    page = context.new_page()
    page.set_default_timeout(15000)
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.wait_for_load_state("networkidle")
    page.get_by_role("button", name="Log In").click()
    page.get_by_test_id("signUp.switchToSignUp").click()
    page.get_by_test_id("siteMembersDialogLayout").get_by_test_id("buttonElement").click()
    page.get_by_test_id("emailAuth").get_by_label("Email").fill("symon.storozhenko@gmail.com")
    page.get_by_label("Password").fill(PASSWORD)
    page.get_by_test_id("submit").get_by_test_id("buttonElement").click()
    page.wait_for_load_state("networkidle")
    context.storage_state(path='state.json')

    yield context


@pytest.fixture()
def login_set_up(context_creation, playwright):
    browser = playwright.chromium.launch(headless=True, slow_mo=200)
    context = browser.new_context(storage_state='state.json')
    page = context.new_page()
    page.set_default_timeout(15000)
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    expect(page.get_by_role("button", name="Log In")).not_to_be_visible()

    yield page
    browser.close()


@pytest.fixture(scope="session")
def go_to_new_collection_page(set_up):
    page = set_up
    page.set_default_timeout(15000)
    page.goto("/new-collection")

    yield page
