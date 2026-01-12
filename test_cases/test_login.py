import allure
import pytest
from web_pages.login_page import LoginPage
from utilities.retries import retry
from utilities.firewall import is_firewall_page
from playwright.sync_api import TimeoutError

@allure.feature("Login")
@allure.story("Negative login attempt with retry")
def test_login_negative(page, base_url):
    login = LoginPage(page)

    with allure.step("Open homepage"):
        page.goto(base_url, wait_until="domcontentloaded", timeout=60000)
        if is_firewall_page(page.content()):
            pytest.skip("Blocked by Optibet firewall in this environment")

    with allure.step("Open login modal"):
        login.open_form()

    with allure.step("Attempt login with invalid credentials (with retry)"):
        retry(
            lambda: login.login("nonexistent@test.com", "wrongpass"),
            exceptions=(TimeoutError,),
            attempts=3,
            delay=1.0
        )

    with allure.step("Verify error message is shown"):
        error = login.get_error().lower()
        print("ERROR TEXT:", error)
        error = login.get_error().lower()
        assert (
            "nepareiz" in error
            or "kaut kas nogāja greizi" in error
            or "kaut kas nogaja greizi" in error  
        )
