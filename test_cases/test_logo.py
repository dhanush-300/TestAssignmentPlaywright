import allure
from web_pages.header_page import HeaderPage

@allure.feature("Header & Language")
def test_logo_and_menu_items(page, base_url):
    header = HeaderPage(page)

    with allure.step("Open main page"):
        page.goto(base_url, wait_until="domcontentloaded", timeout=60000)
        header.accept_cookies()

    with allure.step("Verify logo and menu"):
        assert header.verify_logo()
        header.reveal_full_menu()
        assert header.verify_menu_items()
    
