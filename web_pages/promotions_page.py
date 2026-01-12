from web_pages.base_page import BasePage

class PromotionsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.page = page

    def open_promotions(self):
        self.page.goto("https://www.optibet.lv/", wait_until="domcontentloaded")

        # Step 2: Accept cookies
        try:
            self.page.get_by_role("button", name="Atļaut visu").click(timeout=3000)
        except:
            pass

        self.page.get_by_role("link", name="Piedāvājumi").click()
        self.page.wait_for_selector("[data-testid='promotion-card']", timeout=10000)

    def get_promo_cards(self):
        return self.page.locator("div.promotion-card").count()
