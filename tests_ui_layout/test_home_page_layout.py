import pytest
from playwright.sync_api import Playwright, sync_playwright, expect
from pom.home_page_elements import HomePage
from pom.shop_women_elements import ShopWomen


@pytest.mark.integration
def test_about_us_section_verbiage(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    home_page = HomePage(page)
    shop_women = ShopWomen(page)
    expect(home_page.celebrate_header).to_be_visible()
    expect(shop_women.celebrate_body).to_be_visible()


@pytest.mark.skip(reason="not ready")
def test_about_us_section_verbiage_2(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    home_page = HomePage(page)
    shop_women = ShopWomen(page)
    expect(home_page.celebrate_header).to_be_visible()
    expect(shop_women.celebrate_body).to_be_visible()


@pytest.mark.regression
@pytest.mark.xfail(reason="url not ready")
def test_about_us_section_verbiage_3(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    home_page = HomePage(page)
    shop_women = ShopWomen(page)
    expect(home_page.celebrate_header).to_be_visible()
    expect(shop_women.celebrate_body).to_be_visible()