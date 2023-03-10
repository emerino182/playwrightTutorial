import pytest
from playwright.sync_api import expect


@pytest.mark.smoke
@pytest.mark.regression
def test_login(login_set_up):
    # Asses - Given
    page = login_set_up

    expect(page.get_by_role("button", name="Log In")).to_be_hidden()
    page.locator("// *[ @ id = 'comp-kqx7ocfp5label']").click()
    # page.wait_for_load_state()
    page.wait_for_selector("#comp-kqx72xkk > h1 > span")
    expect(page.get_by_text("Help Center")).to_be_visible()
    print("Yeai")
