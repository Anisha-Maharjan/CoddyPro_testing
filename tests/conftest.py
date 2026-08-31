import os
import pytest
from selenium import webdriver

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.navbar import NavBar
from pages.customer_page import CustomerPage
from pages.product_page import ProductPage
from pages.quotation_page import QuotationPage
from pages.invoice_page import InvoicePage
from pages.purchase_page import PurchasePage

from config import config


FAILURE_ARTIFACTS_DIR = os.path.join(os.path.dirname(__file__), "..", "failure_artifacts")
PASSED_ARTIFACTS_DIR = os.path.join(os.path.dirname(__file__), "..", "passed_artifacts")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Stash the test outcome on the item so the driver fixture can check
    it during teardown (pytest doesn't expose pass/fail to fixtures directly)."""
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)


@pytest.fixture
def driver(request):
    drv = webdriver.Chrome()
    drv.maximize_window()
    yield drv

    failed = getattr(request.node, "rep_call", None) and request.node.rep_call.failed
    passed = getattr(request.node, "rep_call", None) and request.node.rep_call.passed
    safe_name = request.node.name.replace("/", "_").replace("::", "__")

    if failed:
        os.makedirs(FAILURE_ARTIFACTS_DIR, exist_ok=True)
        screenshot_path = os.path.join(FAILURE_ARTIFACTS_DIR, f"{safe_name}.png")
        html_path = os.path.join(FAILURE_ARTIFACTS_DIR, f"{safe_name}.html")
        try:
            drv.save_screenshot(screenshot_path)
            with open(html_path, "w", encoding="utf-8") as f:
                f.write(drv.page_source)
            print(f"\n[failure artifacts] {screenshot_path}\n[failure artifacts] {html_path}")
        except Exception as e:
            print(f"\n[failure artifacts] could not capture: {e}")
    elif passed:
        os.makedirs(PASSED_ARTIFACTS_DIR, exist_ok=True)
        screenshot_path = os.path.join(PASSED_ARTIFACTS_DIR, f"{safe_name}.png")
        try:
            drv.save_screenshot(screenshot_path)
            print(f"\n[passed artifacts] {screenshot_path}")
        except Exception as e:
            print(f"\n[passed artifacts] could not capture: {e}")

    drv.quit()


@pytest.fixture
def login_page(driver):
    return LoginPage(driver)


@pytest.fixture
def dashboard_page(driver):
    return DashboardPage(driver)


@pytest.fixture
def navbar(driver):
    return NavBar(driver)


@pytest.fixture
def customer_page(driver):
    return CustomerPage(driver)


@pytest.fixture
def product_page(driver):
    return ProductPage(driver)


@pytest.fixture
def quotation_page(driver):
    return QuotationPage(driver)


@pytest.fixture
def invoice_page(driver):
    return InvoicePage(driver)


@pytest.fixture
def purchase_page(driver):
    return PurchasePage(driver)


@pytest.fixture
def logged_in_dashboard(driver, login_page, dashboard_page):
    """Common precondition for every test below login: start at the app,
    log in with valid creds, land on the dashboard."""
    login_page.load()
    login_page.login(config.VALID_EMAIL, config.VALID_PASSWORD)
    assert dashboard_page.is_loaded(), "Expected Dashboard to load after valid login"
    return dashboard_page