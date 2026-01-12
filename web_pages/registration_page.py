from web_pages.base_page import BasePage

class RegistrationPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.page = page

        # Correct selectors for /signup page
        self.email = page.get_by_test_id("signupEmail")
        self.password = page.get_by_test_id("signupPassword")
        self.confirm = page.get_by_test_id("signupConfirmPassword")

        # Password rule locators
        self.rule_no_spaces = page.get_by_text("bez atstarpēm vai pēdiņām", exact=False)
        self.rule_latin_only = page.get_by_text("tikai latīņu burti", exact=False)
        self.rule_special_char = page.get_by_text("rakstzīmes", exact=False)
        self.rule_digit = page.get_by_text("cipars", exact=False)
        self.rule_lowercase = page.get_by_text("mazais burts", exact=False)
        self.rule_uppercase = page.get_by_text("lielais burts", exact=False)

    def open_form(self):
        self.page.goto("https://www.optibet.lv/signup", wait_until="domcontentloaded")
        self.page.wait_for_selector("[data-testid='signupEmail']", timeout=15000)

    def fill_form(self, email, password, confirm):
        self.email.fill(email)
        self.password.fill(password)


    def is_rule_highlighted(self, locator):
        class_attr = locator.get_attribute("class") or ""
        return "validation-rule_completed" in class_attr

    def password_rules_visible(self):
        return {
            "no_spaces": self.is_rule_highlighted(self.rule_no_spaces),
            "latin_only": self.is_rule_highlighted(self.rule_latin_only),
            "special_char": self.is_rule_highlighted(self.rule_special_char),
            "digit": self.is_rule_highlighted(self.rule_digit),
            "lowercase": self.is_rule_highlighted(self.rule_lowercase),
            "uppercase": self.is_rule_highlighted(self.rule_uppercase),
        }