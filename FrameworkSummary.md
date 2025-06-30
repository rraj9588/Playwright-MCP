# Playwright-Python Based Test Framework

## Features
- Playwright browser automation (Python)
- Allure reporting for beautiful test results
- Parallel test execution (pytest-xdist)
- Modular, reusable helpers (e.g., login)
- Pytest fixtures for browser/page management
- Test markers for easy categorization
- **Automatic Slack notification of test results**
- **Reusable logging utility with rotating log file and console output**
- **Team-based test organization (BOM & Concurrency)**

## Project Structure
- `tests/` — All test cases and utilities
- `tests/BOM/` — BOM team test cases (reuses all shared utilities)
- `tests/Concurrency/` — Concurrency team test cases (reuses all shared utilities)
- `tests/utils.py` — Reusable helper functions (e.g., login)
- `tests/log_utils.py` — Reusable logging setup for all tests
- `conftest.py` — Pytest fixtures for browser/page
- `pytest.ini` — Pytest configuration (parallel, Allure, markers)
- `requirements.txt` — All dependencies
- `README.md` — Setup and usage instructions
- `send_to_slack.py` — Script to send test results to Slack
- `run_and_notify.sh` — Script to run tests and notify Slack
- `tests/api/test_rest/test_rest_api_examples.py` — Example REST API tests
- `tests/api/test_graphql/test_graphql_api_examples.py` — Example GraphQL API tests
- `archive/` — (Optional) Folder for deprecated or legacy files. You may delete its contents if not needed.

## Step-by-Step Setup Instructions
1. **Clone the repository and enter the project directory.**
   ```bash
   git clone <your-repo-url>
   cd Playwright-MCP
   ```
2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   playwright install
   ```
4. **(Optional) Install Allure CLI for report viewing:**
   - On macOS (with Homebrew): `brew install allure`
   - Or follow manual instructions from the [Allure website](https://docs.qameta.io/allure/)

## Running Tests and Sharing Results on Slack
1. **Make the run script executable (first time only):**
   ```bash
   chmod +x run_and_notify.sh
   ```
2. **Run all tests and automatically notify Slack:**
   ```bash
   ./run_and_notify.sh
   ```
3. **To view the Allure report:**
   ```bash
   allure serve allure-results
   ```

## Running Selective Tests
- **By marker (e.g., only BOM team tests):**
  ```bash
  pytest -m bom
  ```
- **By test file:**
  ```bash
  pytest tests/BOM/test_bom_example.py
  ```
- **By test function name (substring match, e.g., any test with 'concurrency' in its name):**
  ```bash
  pytest -k "concurrency"
  ```
- **By exact test function name:**
  ```bash
  pytest -k "test_concurrency_example"
  ```
- **By group/marker and function name (e.g., all Concurrency team tests with 'example' in the name):**
  ```bash
  pytest -m concurrency -k "example"
  ```
- **Combine with Slack notification:**
  ```bash
  pytest -m bom > result.txt
  python send_to_slack.py
  ```

## Logging
- All tests can use the reusable logging setup by importing and calling `setup_logging()` from `tests/log_utils.py`.
- Logs are written to both the console and a rotating file `test_run.log` (with backups).

## Adding Tests (For Any Team)
1. **Create your test file in your team folder:**
   - For BOM: `tests/BOM/`
   - For Concurrency: `tests/Concurrency/`
2. **At the top of your test file, add:**
   ```python
   from tests.log_utils import setup_logging
   setup_logging()
   ```
3. **Write your test using pytest, Allure, and logging as needed.**
4. **Use markers like `@pytest.mark.login`, `@pytest.mark.smoke`, `@pytest.mark.bom`, and `@pytest.mark.concurrency` for organization.**

## Housekeeping
- If you see any old files (such as `tests/test_api_examples.py` or files in the `archive/` folder) that are not part of the new structure, you can safely delete them.
- Keep the example test files in each folder as templates for new tests and onboarding.

## Example Tests
- The `tests/BOM/`, `tests/Concurrency/`, `tests/api/test_rest/`, and `tests/api/test_graphql/` folders contain example tests demonstrating:
  - Basic assertions and logging
  - Smoke, regression, and edge case markers
  - UI automation with Playwright and Allure HTML attachments
  - Data-driven testing with `pytest.mark.parametrize`
  - REST API validation with `requests`
  - GraphQL API validation with `requests`
  - Allure step usage and advanced reporting

**Do not delete the example test files.**
- These serve as templates and references for writing new tests and for onboarding new team members.
- You can add your own tests alongside these examples.

## Advanced Topics

### Data-Driven and Parametrized Testing
- Use `pytest.mark.parametrize` to run the same test logic with multiple sets of data (see BOM and Concurrency example files).
- Combine with Allure steps and attachments for rich reporting.

### Workflow Simulation and Stepwise Validation
- Simulate real-world business workflows in tests, using Allure steps to document each phase (see `test_bom_workflow_simulation`).
- Attach intermediate and final data as JSON or text for traceability.

### Concurrency and Parallelism
- Use `pytest-xdist` for parallel test execution: `pytest -n auto` or specify workers.
- Write tests that simulate concurrent users, race conditions, or resource contention (see Concurrency example file).

### UI and API Test Integration
- Mix UI and API calls in a single test to validate end-to-end flows.
- Use Playwright for browser automation and `requests` for API validation.

### Logging and Debugging
- Use the reusable logging setup for detailed logs in both console and file.
- Attach logs or screenshots to Allure reports for failed steps.

### CI/CD Integration (Optional)
- Integrate with GitHub Actions, GitLab CI, or Jenkins for automated test runs.
- Publish Allure reports and Slack notifications as part of your pipeline.

### Test Data Management (Optional)
- Store test data in separate files (YAML, JSON, CSV) and load dynamically in tests.
- Use fixtures to manage setup/teardown of test data.

### Environment Configuration (Optional)
- Use environment variables or config files to manage URLs, credentials, and other settings.
- Add a `.env` file at the project root (see `.env.example`) and set environment variables for URLs, credentials, and secrets.
- Reference environment variables in your tests and helpers using `os.environ.get()` (see BOM and Concurrency example files).
- Example:
  ```python
  import os
  BASE_URL = os.environ.get('BASE_URL', 'https://example.com')
  ```
- Do not hardcode sensitive or environment-specific data in test files.

## CI/CD with Jenkins

A sample `Jenkinsfile` is included for automated test execution:
- **Setup**: Installs dependencies and Playwright browsers in a virtual environment.
- **Smoke Tests**: Runs all tests marked with `@pytest.mark.smoke`, generates Allure and JUnit XML reports, and archives results.
- **E2E Tests**: Runs all tests marked with `@pytest.mark.e2e`, generates Allure and JUnit XML reports, and archives results.
- **API Tests**: Runs all tests marked with `@pytest.mark.api`, generates Allure and JUnit XML reports, and archives results.
- **Test Results**: Jenkins publishes JUnit XML results for all stages.
- **Allure Reports**: Allure results are published if the Allure Jenkins plugin is installed.
- **Cleanup**: Cleans up virtual environment and result folders after the build.
- **Slack Notifications**: Sends build status notifications to Slack channel `#test-result` (requires Slack Jenkins plugin and configuration).

Example pipeline stages:
```groovy
stage('Smoke Tests') {
    steps {
        sh 'source $VENV_DIR/bin/activate && pytest -m smoke --alluredir=allure-results-smoke --junitxml=allure-results-smoke/junit-smoke.xml'
    }
}
stage('E2E Tests') {
    steps {
        sh 'source $VENV_DIR/bin/activate && pytest -m e2e --alluredir=allure-results-e2e --junitxml=allure-results-e2e/junit-e2e.xml'
    }
}
stage('API Tests') {
    steps {
        sh 'source $VENV_DIR/bin/activate && pytest -m api --alluredir=allure-results-api --junitxml=allure-results-api/junit-api.xml'
    }
}
post {
    always {
        junit 'allure-results-*/junit-*.xml'
        allure([
            includeProperties: false,
            jdk: '',
            results: [[path: 'allure-results-smoke']],
            reportBuildPolicy: 'ALWAYS',
            results: [[path: 'allure-results-e2e']],
            results: [[path: 'allure-results-api']]
        ])
    }
    cleanup {
        sh 'rm -rf $VENV_DIR allure-results-*'
    }
    success {
        slackSend(channel: '#test-result', color: 'good', message: "Build SUCCESS: ${env.JOB_NAME} #${env.BUILD_NUMBER}")
    }
    failure {
        slackSend(channel: '#test-result', color: 'danger', message: "Build FAILURE: ${env.JOB_NAME} #${env.BUILD_NUMBER}")
    }
}
```

## Test Context Directory (`testcontext/`)
The `testcontext/` folder is used to store shared test context, data, or state that may be needed across multiple tests or by different teams. For example, you can place files like `webtestcontext.txt` or other context/configuration files here. This enables tests to:
- Share setup or state between UI, API, and workflow tests
- Store temporary data or artifacts needed for multi-step or cross-team scenarios
- Keep context files out of the main test directories for better organization

> **Best Practice:** Clean up or version-control only essential context files. Avoid storing sensitive data here.

## Playwright MCP (Model Context Protocol) Usage (Advanced)

Playwright's Model Context Protocol (MCP) is an advanced feature for sharing browser and test context between tools and processes.

- MCP is typically used in large-scale, distributed, or cross-language automation scenarios.
- Python Playwright does not natively expose MCP APIs, but you can use Playwright's CLI or Node.js server to interact with MCP endpoints if needed.
- For most UI/API automation, you do not need to configure MCP.

### How to Use Playwright MCP (Advanced)
1. Refer to the official Playwright documentation: https://playwright.dev/docs/mcp
2. Use the Playwright CLI or Node.js server to start an MCP endpoint.
3. Connect your Python tests to the MCP endpoint using Playwright's remote browser capabilities.

**Example (Node.js MCP server):**
```bash
npx playwright mcp-server --port=9000
```

**Example (Python connect to MCP):**
```python
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.connect_over_cdp('ws://localhost:9000')
    # ...run tests using the remote browser...
```

> Note: This is an advanced feature and not required for most test automation workflows.
