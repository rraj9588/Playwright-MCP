from playwright.sync_api import Page
import allure

def login_chameleon_autodesk(page: Page, email: str, password: str):
    with allure.step("Waiting for email input"):
        page.wait_for_selector('input#userName', timeout=20000)
    with allure.step("Filling email"):
        page.fill('input#userName', email)
    with allure.step("Clicking Next"):
        page.click('button#verify_user_btn')
    with allure.step("Waiting for password input"):
        try:
            page.wait_for_selector('input[type="password"]', timeout=20000)
        except Exception as e:
            allure.attach(page.content(), name="page_content", attachment_type=allure.attachment_type.HTML)
            raise AssertionError(f"Password input not found: {e}")
    with allure.step("Filling password"):
        page.fill('input[type="password"]', password)
    with allure.step("Clicking submit"):
        page.click('button[type="submit"]')
    # No wait for landing page
