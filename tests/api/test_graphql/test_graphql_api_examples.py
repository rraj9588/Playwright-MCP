import pytest
import allure
import logging
import requests
from tests.log_utils import setup_logging

setup_logging()

@allure.feature('API')
@allure.story('GraphQL API Basic Test')
@pytest.mark.api
@pytest.mark.graphql
def test_graphql_api_query():
    url = "https://countries.trevorblades.com/"
    query = '{ country(code: "IN") { name capital currency } }'
    logging.info(f"Sending GraphQL query to {url}")
    with allure.step(f"POST {url}"):
        response = requests.post(url, json={"query": query})
        allure.attach(str(response.text), name="GraphQL Response", attachment_type=allure.attachment_type.JSON)
        assert response.status_code == 200
        assert "India" in response.text
