from playwright.sync_api import Playwright, sync_playwright, expect
from home_page_elements import HomePage
from shop_women_elements import ShopWomen


def about_us_section_verbiage(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    home_page = HomePage(page)
    shop_women = ShopWomen(page)
    expect(home_page.celebrate_header).to_be_visible()
    expect(shop_women.celebrate_body).to_be_visible()


with sync_playwright() as playwright:
    about_us_section_verbiage(playwright)
