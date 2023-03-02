

class ContactUsPage:
    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto("https://symonstorozhenko.wixsite.com/website-1/contact")

    def submit_form(self, name, address, email, phone, subject, text):
        self.page.get_by_placeholder("Enter your name").fill(name)
        self.page.get_by_placeholder("Enter your address").fill(address)
        self.page.get_by_placeholder("Enter your email").fill(email)
        self.page.get_by_placeholder("Enter your phone number").fill(phone)
        self.page.get_by_placeholder("Type the subject").fill(subject)
        self.page.get_by_placeholder("Type your message here...").fill(text)
        # self.page.get_by_test_id("buttonElement").click()
