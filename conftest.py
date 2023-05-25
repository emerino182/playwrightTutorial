import pytest


@pytest.fixture(scope="session")
def context_creation(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    context.storage_state(path='state.json')

    yield context


@pytest.fixture()
def page_set_up(context_creation):
    context = context_creation
    page = context.new_page()

    yield page


@pytest.fixture()
def login_set_up(context_creation):
    context = context_creation
    page = context.new_page()
    page.goto("https://qa-accounts.consumeraffairs.com/")
    page.get_by_placeholder("Email address").fill("emerino@consumeraffairs.com")
    page.get_by_role("button", name="Continue").click()
    page.get_by_placeholder("Password").fill("cAgtlpn7!182")
    page.get_by_role("button", name="Login").click()

    yield page
