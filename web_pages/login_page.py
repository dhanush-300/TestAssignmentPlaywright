from playwright.sync_api import TimeoutError

class LoginPage:
    def __init__(self, page):
        self.page = page

        self.email = page.get_by_test_id("loginEmailInput")
        self.password = page.get_by_test_id("password")

        self.submit = page.get_by_text("IenāktAizmirsi paroli?", exact=False)

        self.toast_error = page.locator(
            "div[role='alert'], div.toast, div[class*='toast'], div[class*='notification']"
        )

        self.modal_container = page.locator("[data-testid='loginEmailInput']")
        self.modal_error = page.locator("text=/Nepareizs|nepareiz/i")
        self.generic_error = page.locator("text=/Kaut kas nog(ā|a)ja greizi/i")


    def open_form(self):
        if self.modal_container.first.is_visible():
            return

        self.page.get_by_role("button", name="Ienākt").first.click()
        self.page.wait_for_selector("[data-testid='loginEmailInput']", timeout=15000)


    def login(self, email: str, password: str):
        self.page.wait_for_selector("[data-testid='loginEmailInput']", timeout=15000)

        self.email.fill(email)
        self.password.fill(password)

        self.submit.click()


    def get_error(self):
        if self.toast_error.first.is_visible():
            return self.toast_error.first.inner_text().strip()

        if self.modal_error.first.is_visible():
            return self.modal_error.first.inner_text().strip()
        
        if self.generic_error.first.is_visible():
            return self.generic_error.first.inner_text().strip()

        return ""