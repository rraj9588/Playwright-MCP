import os
import pytest
import allure
from tests.utils import login_chameleon_autodesk

CHAMELEON_URL = os.environ.get("CHAMELEON_URL", "https://demo.chameleon.autodesk.com/")
CHAMELEON_USER = os.environ.get("CHAMELEON_USER", "smoke_testuser004@ssttest.net")
CHAMELEON_PASS = os.environ.get("CHAMELEON_PASS", "Testing@123")

@allure.feature('Login')
@allure.story('Chameleon Autodesk Login')
@pytest.mark.login
@pytest.mark.smoke
def test_login_chameleon_autodesk(page):
    with allure.step("Navigate to login page"):
        page.goto(CHAMELEON_URL)
    with allure.step("Perform login"):
        login_chameleon_autodesk(page, CHAMELEON_USER, CHAMELEON_PASS)
