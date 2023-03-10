import pytest
from playwright.sync_api import Playwright, sync_playwright, expect
from pom.home_page_elements import HomePage
from pom.shop_women_elements import ShopWomen


@pytest.mark.integration
def test_about_us_section_verbiage(set_up):
    page = set_up
    home_page = HomePage(page)
    shop_women = ShopWomen(page)
    expect(home_page.celebrate_header).to_be_visible()
    expect(shop_women.celebrate_body).to_be_visible()


@pytest.mark.skip(reason="not ready")
def test_about_us_section_verbiage_2(set_up):
    page = set_up
    home_page = HomePage(page)
    shop_women = ShopWomen(page)
    expect(home_page.celebrate_header).to_be_visible()
    expect(shop_women.celebrate_body).to_be_visible()


@pytest.mark.regression
@pytest.mark.xfail(reason="url not ready")
def test_about_us_section_verbiage_3(set_up):
    page = set_up
    home_page = HomePage(page)
    shop_women = ShopWomen(page)
    expect(home_page.celebrate_header).to_be_visible()
    expect(shop_women.celebrate_body).to_be_visible()