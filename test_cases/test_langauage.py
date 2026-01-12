import allure
from web_pages.header_page import HeaderPage
import pytest


@pytest.mark.skip("Language switching is not functional on playwright browser due to firewall/security restrictions.")
@allure.feature("Header & Language")
def test_language_switcher(page, base_url):
    header = HeaderPage(page)

    with allure.step("Open main page"):
        page.goto(base_url, wait_until="domcontentloaded", timeout=60000)
        header.accept_cookies()

    for lang in ["LV", "EN", "RU", "LV"]:
        header.switch_language(lang)
        assert header.get_active_language() == lang

    
    # Also tested with playwright codegen ui browser, same issue. 
    # 89.221.127.174 
    # 9b9ec4479dd4340e 
    # LV Ja uzskatāt, 
    # ka šo ziņojumu saņēmāt kļūdas dēļ, lūdzu, sazinieties ar mums: support@optibet.lv 
    # If you beeived this message in error, please contact: support@optibet.lv 
    # Если вы считаете, что получили это сообщение по ошибке, пожалуйста, свяжитесь с нами: support@optibet.lv.
    
