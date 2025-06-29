import pytest
import allure
import logging
import requests
from tests.log_utils import setup_logging

setup_logging()

@allure.feature('API')
@allure.story('REST API Basic Test')
@pytest.mark.api
@pytest.mark.rest
def test_rest_api_get():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    logging.info(f"Sending GET request to {url}")
    with allure.step(f"GET {url}"):
        response = requests.get(url)
        allure.attach(str(response.text), name="Response Body", attachment_type=allure.attachment_type.TEXT)
        assert response.status_code == 200
        assert "userId" in response.text
