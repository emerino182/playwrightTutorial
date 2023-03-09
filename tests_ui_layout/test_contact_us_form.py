from pom.contact_us_page import ContactUsPage


def test_submit_form(set_up):
    page = set_up
    contact_page = ContactUsPage(page)
    contact_page.navigate()
    contact_page.submit_form("Lalo Merino", "My home", "this@mail.com", "4491552969", "Subject", "Message")

