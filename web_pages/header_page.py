from .base_page import BasePage
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError

class HeaderPage(BasePage):

    logo = "img[alt='Optibet']"

    language_button = "#languageSelector .current-language"
    language_option = ".language-selector__dropdown a[data-lang='{}']"
    language_dropdown = "select#language"
    language_toggle = ".language-selector__toggle"
    menu_toggle = "button.header-menu__toggle"


    def topbar(self):
        return self.page.frame_locator("#topBarIframe")

    # Stable, language‑independent selectors using data-role
    menu_items = {
    "Casino": "#topBar >> role=link[name='Kazino']",
    "Sports": "#topBar >> role=link[name='Sports']",
    "Live Casino": "role=link[name='Live kazino']",
    "Esports": "role=link[name='E-Sports']",
    "Poker": "#topBar >> role=link[name='Pokers']",
    "Promotions": "role=link[name='Piedāvājumi']"
    }


    def verify_logo(self):
        try:
            self.page.get_by_role("link").first.wait_for(state="visible", timeout=5000)
            return True
        except:
            return False



    def verify_menu_items(self):
        for name, selector in self.menu_items.items():
            try:
                self.page.locator(selector).wait_for(state="visible", timeout=5000)
            except:
                print(f"Menu item not visible: {name} ({selector})")
                return False
        return True


    def switch_language(self, lang):
        self.page.locator("button.header-menu__toggle").click()
        self.page.locator("nav.header-menu__content").wait_for(state="visible")
        self.page.locator(f"a[data-id='langMenuItem-{lang.lower()}']").click()


    def get_active_language(self):
        return self.page.locator("a.language-menu__language-item--active").inner_text().upper()


    def accept_cookies(self):
        btn = self.page.get_by_role("button", name="Atļaut visu")
        if btn.is_visible():
            btn.click()


    def reveal_full_menu(self):
        """
        Scrolls down slightly to trigger the sticky header
        where Casino, Live Casino, Poker, Esports, Promotions appear.
        """
        self.page.mouse.wheel(0, 400)