import pytest
import allure
from playwright.sync_api import Playwright
from utilities.stealth import apply_stealth


def pytest_addoption(parser):
    parser.addoption("--base_url", action="store", default="https://www.optibet.lv/")
    # DO NOT add --headed or --browser-channel (Playwright already provides them)


@pytest.fixture(scope="session")
def base_url(pytestconfig):
    return pytestconfig.getoption("--base_url")


@pytest.fixture(scope="session")
def browser(playwright: Playwright, pytestconfig):
    headed = pytestconfig.getoption("--headed")          # ← YOU MUST HAVE THIS
    channel = pytestconfig.getoption("--browser-channel")

    browser = playwright.chromium.launch(
        headless=not headed,
        channel=channel,
        args=[
            "--headless=new" if not headed else "",
            "--disable-blink-features=AutomationControlled",
            "--disable-web-security",
            "--disable-features=IsolateOrigins,site-per-process",
            "--disable-dev-shm-usage",
            "--no-sandbox",
            "--disable-infobars",
            "--disable-notifications",
            "--disable-popup-blocking",
        ],
    )
    yield browser
    browser.close()


@pytest.fixture()
def context(browser):
    context = browser.new_context(
        viewport={"width": 1920, "height": 1080},
        user_agent=(
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0.0.0 Safari/537.36"
        ),
        java_script_enabled=True,
        bypass_csp=True,
        locale="lv-LV",
        permissions=["geolocation"],
    )

    # Apply stealth mode
    apply_stealth(context)

    return context



@pytest.fixture()
def page(context, request):
    page = context.new_page()
    yield page

    # Attach Allure artifacts on failure
    rep = getattr(request.node, "rep_call", None)
    if rep and rep.failed:
        try:
            allure.attach(
                page.screenshot(full_page=True),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG,
            )
        except Exception:
            pass

        try:
            allure.attach(
                page.content(),
                name="page_source",
                attachment_type=allure.attachment_type.HTML,
            )
        except Exception:
            pass


def pytest_runtest_makereport(item, call):
    if "page" in item.fixturenames:
        item.rep_call = call