import pytest
import allure
import logging
import os
from tests.log_utils import setup_logging

setup_logging()

BASE_URL = os.environ.get("BASE_URL", "https://example.com")
PYTHON_ORG_URL = os.environ.get("PYTHON_ORG_URL", "https://www.python.org")

@allure.feature('Concurrency')
@pytest.mark.concurrency
def test_concurrency_example():
    logging.info("Running Concurrency team example test.")
    assert True

@allure.feature('Concurrency')
@allure.story('Concurrency Smoke Test')
@pytest.mark.concurrency
@pytest.mark.smoke
def test_concurrency_smoke():
    logging.info("Running Concurrency smoke test.")
    assert True

@allure.feature('Concurrency')
@allure.story('Concurrency Edge Case')
@pytest.mark.concurrency
@pytest.mark.edgecase
def test_concurrency_edgecase():
    logging.info("Running Concurrency edge case test.")
    assert 2 * 2 == 4

# --- Advanced Topics for Concurrency Testing ---
# Example: Data-driven concurrency test with parametrize and Allure steps
import time

@allure.feature('Concurrency')
@allure.story('Data-Driven Concurrency')
@pytest.mark.concurrency
@pytest.mark.parametrize("user_count", [1, 5, 10])
def test_concurrent_users(user_count):
    """Simulate multiple users performing actions concurrently."""
    logging.info(f"Simulating {user_count} concurrent users.")
    with allure.step(f"Start {user_count} user sessions concurrently"):
        # Simulate concurrent actions (replace with real logic as needed)
        results = []
        for i in range(user_count):
            logging.info(f"User {i+1} starts action.")
            # Simulate user action (e.g., API call, UI interaction)
            results.append(True)
            time.sleep(0.1)  # Simulate slight delay per user
        assert all(results)
        allure.attach(str(results), name="User Results", attachment_type=allure.attachment_type.TEXT)

# Example: Use BASE_URL and PYTHON_ORG_URL from environment variables in a test
@allure.feature('Concurrency')
@allure.story('Environment Config Example')
@pytest.mark.concurrency
def test_environment_config_usage():
    logging.info(f"BASE_URL from env: {BASE_URL}")
    logging.info(f"PYTHON_ORG_URL from env: {PYTHON_ORG_URL}")
    assert BASE_URL.startswith("http")
    assert PYTHON_ORG_URL.startswith("http")

# Example: Simulate race condition or resource contention
@allure.feature('Concurrency')
@allure.story('Race Condition Simulation')
@pytest.mark.concurrency
@pytest.mark.critical
def test_race_condition_simulation():
    logging.info("Simulating race condition scenario.")
    shared_resource = {"counter": 0}
    def increment():
        val = shared_resource["counter"]
        time.sleep(0.05)  # Simulate processing delay
        shared_resource["counter"] = val + 1
    for _ in range(5):
        increment()
    assert shared_resource["counter"] == 5
    allure.attach(str(shared_resource), name="Final Counter", attachment_type=allure.attachment_type.TEXT)
