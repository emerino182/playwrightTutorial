import pytest
from pom.auto_warranties_flow import AutoWarrantiesFlow


@pytest.mark.smoke
def test_auto_warranties_catch_all(page_set_up):
    page = page_set_up

    auto_warranties = AutoWarrantiesFlow(page)
    auto_warranties.navigate()
    auto_warranties.select_year()
    auto_warranties.select_make()
    auto_warranties.select_model()
    auto_warranties.select_mileage()
    auto_warranties.select_aw_purchase_process()
    auto_warranties.select_include_perks()
    auto_warranties.select_roadside_assistance()
    auto_warranties.select_currently_need_repairs()
    auto_warranties.enter_zip_using_warranty()
    auto_warranties.select_discounts_offers()
    auto_warranties.enter_email()
    auto_warranties.submit_pii()
    auto_warranties.confirm_no_match()

    page.close()


@pytest.mark.parametrize("config_num", [pytest.param("?config_id=472", marks=pytest.mark.xfail)])
def test_auto_warranties_specific_config(page_set_up, config_num):
    page = page_set_up

    auto_warranties = AutoWarrantiesFlow(page)
    auto_warranties.navigate(config_num)
    auto_warranties.select_year()
    auto_warranties.select_make()
    auto_warranties.select_model()
    auto_warranties.select_mileage()
    auto_warranties.select_aw_purchase_process()
    auto_warranties.select_include_perks()
    auto_warranties.select_roadside_assistance()
    auto_warranties.select_currently_need_repairs()
    auto_warranties.enter_zip_using_warranty()
    auto_warranties.select_discounts_offers()
    auto_warranties.enter_email()
    auto_warranties.submit_pii()
    auto_warranties.confirm_no_match()

    page.close()
