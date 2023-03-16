from pom.home_page_elements import HomePage
from playwright.sync_api import expect


def test_visual_landing_2_1(page, assert_snapshot):
    # Asses  Given
    page.goto("https://symonstorozhenko.wixsite.com/website-1/shop")
    homepage = HomePage(page)
    expect(homepage.celebrate_header).not_to_be_visible()
    assert_snapshot(page.screenshot(full_page=True, mask=[homepage.cart_icon]), threshold=1, fail_fast=True)


def test_visual_landing_2_2(page, assert_snapshot):
    # Asses  Given
    page.goto("https://symonstorozhenko.wixsite.com/website-1/")
    homepage = HomePage(page)
    expect(homepage.celebrate_header).to_be_visible()
    assert_snapshot(page.screenshot())
