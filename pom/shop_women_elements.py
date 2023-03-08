

class ShopWomen:
    def __init__(self, page):
        self.celebrate_header = page.get_by_text("Celebrating Beauty and Style")
        self.celebrate_body = page\
            .get_by_text("playwright-practice was founded by a group of like-minded fashion devotees, dete")


# NAMING CONVENTIONS
# packages/folders : "test*";, "tests_ui_layout"
# python files: "tests*", "test_home_page_layout"
# python functions/modules: "test*", "test_about_us_sections_verbiage"
# python classes: "Test*", "TestHomePage"
