from playwright.sync_api import Playwright, sync_playwright, expect
from pom.contact_us_page import ContactUsPage


def test_submit_form(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    contact_page = ContactUsPage(page)
    contact_page.navigate()
    contact_page.submit_form("Lalo Merino", "My home", "this@mail.com", "4491552969", "Subject", "Message")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    test_submit_form(playwright)
