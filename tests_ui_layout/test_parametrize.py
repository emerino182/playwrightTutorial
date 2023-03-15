import pytest
from playwright.sync_api import expect


@pytest.mark.parametrize("email", ["symon.storozhenko@gmail.com",
                                   pytest.param("fakemail", marks=pytest.mark.xfail),
                                   pytest.param("symon.storozhenko@gmail", marks=pytest.mark.xfail)])
@pytest.mark.parametrize("password", ["test123",
                                      pytest.param("fakepassword", marks=pytest.mark.xfail),
                                      pytest.param("test123", marks=pytest.mark.xfail)])
def test_user_can_login(set_up, email, password):
    # Asses - Given
    page = set_up

    page.wait_for_load_state("networkidle")
    page.get_by_role("button", name="Log In").click()
    page.get_by_test_id("signUp.switchToSignUp").click()
    page.get_by_test_id("siteMembersDialogLayout").get_by_test_id("buttonElement").click()
    page.get_by_test_id("emailAuth").get_by_label("Email").fill(email)
    page.get_by_label("Password").fill(password, timeout=3000)
    page.get_by_test_id("submit").get_by_test_id("buttonElement").click()
    page.wait_for_load_state("networkidle")
    expect(page.get_by_role("button", name="Log In")).to_be_hidden()
    page.locator("// *[ @ id = 'comp-kqx7ocfp5label']").click()
    # page.wait_for_load_state()
    page.wait_for_selector("#comp-kqx72xkk > h1 > span")
    expect(page.get_by_text("Help Center")).to_be_visible()
    print("Yeai")