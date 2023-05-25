from playwright.sync_api import expect


class AutoWarrantiesFlow:
    def __init__(self, page):
        self.page = page

    def navigate(self, config=""):
        self.page.goto("https://qa-my.consumeraffairs.com/auto-warranties/" + config)

    def select_year(self):
        self.page.locator("label").filter(has_text="2021").click()

    def select_make(self):
        self.page.locator("label").filter(has_text="HONDA").click()

    def select_model(self):
        self.page.locator("label").filter(has_text="Civic").first.click()

    def select_mileage(self):
        self.page.locator("label").filter(has_text="Less than 100K").click()

    def select_aw_purchase_process(self):
        self.page.get_by_text("None apply to me").click()

    def select_include_perks(self):
        self.page.locator("label").filter(has_text="YES").click()

    def select_roadside_assistance(self):
        self.page.locator("#qf_step_7 label").filter(has_text="YES").click()

    def select_currently_need_repairs(self):
        self.page.locator("#qf_step_8 label").filter(has_text="NO").click()

    def enter_zip_using_warranty(self):
        self.page.get_by_placeholder("ZIP Code").fill("78757")
        self.page.get_by_role("button", name="Next").click()

    def select_discounts_offers(self):
        self.page.locator("#qf_step_10").get_by_text("None apply to me").click()

    def enter_email(self):
        self.page.get_by_placeholder("email@address.com").fill("qa.05242023.1254@consumeraffairs.com")
        self.page.get_by_role("button", name="Final step").click()

    def submit_pii(self):
        self.page.get_by_placeholder("First name").fill("QA Lalo")
        self.page.get_by_placeholder("Last name").fill("QA Merino")
        self.page.get_by_placeholder("Phone #").fill("918-660-0530")
        self.page.get_by_role("button", name="See My Match").click()

    def confirm_no_match(self):
        expect(self.page.get_by_role("heading", name="Sorry, there was an issue")).to_be_visible(timeout=10000)
