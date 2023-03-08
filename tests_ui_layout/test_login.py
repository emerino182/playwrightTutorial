from playwright.sync_api import Playwright, sync_playwright, expect


def test_login(playwright: Playwright) -> None:
    # browser = playwright.chromium.launch(headless=False, slow_mo=500)
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.set_default_timeout(15000)
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.wait_for_load_state("networkidle")
    page.get_by_role("button", name="Log In").click()
    # page.get_by_text("Log In").click()
    # login_issue = True
    # while login_issue:
    #     if not page.get_by_test_id("signUp.switchToSignUp").is_visible():
    #         page.get_by_role("button", name="Log In").click()
    #     else:
    #         login_issue = False
    page.get_by_test_id("signUp.switchToSignUp").click()
    page.get_by_test_id("siteMembersDialogLayout").get_by_test_id("buttonElement").click()
    # page.get_by_test_id("emailAuth").get_by_label("Email").click()
    # page.locator("input:below(:text('Email'))").fill("symon.storozhenko@gmail.com")
    page.get_by_test_id("emailAuth").get_by_label("Email").fill("symon.storozhenko@gmail.com")
    # page.get_by_label("Password").click()
    page.get_by_label("Password").fill("test123", timeout=3000)
    page.get_by_test_id("submit").get_by_test_id("buttonElement").click()
    page.wait_for_load_state("networkidle")
    expect(page.get_by_role("button", name="Log In")).to_be_hidden()
    page.locator("// *[ @ id = 'comp-kqx7ocfp5label']").click()
    # page.wait_for_load_state()
    page.wait_for_selector("#comp-kqx72xkk > h1 > span")
    expect(page.get_by_text("Help Center")).to_be_visible()
    print("Yeai")

    # ---------------------
    context.close()
    browser.close()
