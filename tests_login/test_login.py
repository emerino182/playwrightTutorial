import pytest
from playwright.sync_api import expect


@pytest.mark.regression
def test_logout(login_set_up):
    # Asses - Given
    page = login_set_up

    page.get_by_role("link", name="Logout").click()
    expect(page.get_by_role("button", name="Continue")).to_be_visible()

    page.close()


@pytest.mark.smoke
@pytest.mark.regression
def test_login(login_set_up):
    # Asses - Given
    page = login_set_up

    expect(page.get_by_role("link", name="Logout")).to_be_visible()

    page.close()