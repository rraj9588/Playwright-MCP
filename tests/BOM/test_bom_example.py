import pytest
import allure
import logging
import os
from tests.log_utils import setup_logging
from playwright.sync_api import sync_playwright

setup_logging()

BASE_URL = os.environ.get("BASE_URL", "https://example.com")
PYTHON_ORG_URL = os.environ.get("PYTHON_ORG_URL", "https://www.python.org")

@allure.feature('BOM')
@allure.story('BOM Example Test')
@pytest.mark.bom
def test_bom_example():
    logging.info("Running BOM team example test.")
    assert True

@allure.feature('BOM')
@allure.story('BOM Smoke Test')
@pytest.mark.bom
@pytest.mark.smoke
def test_bom_smoke():
    logging.info("Running BOM smoke test.")
    assert 1 + 1 == 2

@allure.feature('BOM')
@allure.story('BOM Regression Test')
@pytest.mark.bom
@pytest.mark.regression
def test_bom_regression():
    logging.info("Running BOM regression test.")
    assert 'bom' in 'playwright bom test'

@allure.feature('BOM')
@allure.story('BOM UI Test')
@pytest.mark.bom
@pytest.mark.ui
def test_bom_ui_navigation():
    logging.info("Running BOM UI navigation test with Playwright.")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        with allure.step("Navigate to example.com"):
            page.goto("https://example.com")
            allure.attach(page.content(), name="Landing Page HTML", attachment_type=allure.attachment_type.HTML)
        with allure.step("Check page title"):
            title = page.title()
            logging.info(f"Page title: {title}")
            assert "Example Domain" in title
        browser.close()

@allure.feature('BOM')
@allure.story('BOM Data Driven Test')
@pytest.mark.bom
@pytest.mark.parametrize("input_str,expected", [
    ("playwright", True),
    ("bom", True),
    ("missing", False)
])
def test_bom_data_driven(input_str, expected):
    logging.info(f"Running BOM data-driven test with input: {input_str}")
    assert (input_str in "playwright bom test") == expected

# --- Advanced Topics for BOM Testing ---
# Example: Data-driven UI test with parametrize and Allure steps
@allure.feature('BOM')
@allure.story('BOM Data-Driven UI Test')
@pytest.mark.bom
@pytest.mark.parametrize("url,expected_title", [
    (BASE_URL, "Example Domain"),
    (PYTHON_ORG_URL, "Welcome to Python.org"),
])
def test_bom_data_driven_ui(url, expected_title):
    logging.info(f"Navigating to {url} and checking title.")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        with allure.step(f"Navigate to {url}"):
            page.goto(url)
            allure.attach(page.content(), name=f"{url} HTML", attachment_type=allure.attachment_type.HTML)
        with allure.step("Check page title"):
            title = page.title()
            logging.info(f"Page title: {title}")
            assert expected_title in title
        browser.close()

# Example: Simulate BOM workflow with Allure steps and attachments
@allure.feature('BOM')
@allure.story('BOM Workflow Simulation')
@pytest.mark.bom
def test_bom_workflow_simulation():
    logging.info("Simulating BOM workflow steps.")
    with allure.step("Step 1: Prepare data"):
        data = {"item": "widget", "qty": 10}
        allure.attach(str(data), name="Prepared Data", attachment_type=allure.attachment_type.JSON)
    with allure.step("Step 2: Process data"):
        processed = {**data, "status": "processed"}
        allure.attach(str(processed), name="Processed Data", attachment_type=allure.attachment_type.JSON)
    with allure.step("Step 3: Validate output"):
        assert processed["status"] == "processed"
