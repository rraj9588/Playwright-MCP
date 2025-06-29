import pytest
import allure
import logging
from playwright.sync_api import sync_playwright
from tests.log_utils import setup_logging

setup_logging()

@allure.feature('Navigation')
@allure.story('Navigate and Click Products')
@pytest.mark.navigation
@pytest.mark.smoke
def test_navigate_and_click_products():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        with allure.step("Navigate to the website"):
            logging.info("Navigating to https://www.automationexercise.com/")
            page.goto("https://www.automationexercise.com/")
        with allure.step("Click on 'Products'"):
            logging.info("Clicking on 'Products' link")
            page.click('a:has-text("Products")')
        with allure.step("Assert navigation to products page"):
            logging.info(f"Current URL after click: {page.url}")
            assert page.url == "https://www.automationexercise.com/products"
        browser.close()
