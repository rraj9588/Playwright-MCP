[![MIT License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen)](https://github.com/<your-username>/playwright-ui-framework/actions)
[![Coverage Status](https://img.shields.io/badge/coverage-100%25-brightgreen)](https://github.com/<your-username>/playwright-ui-framework)

# Playwright Python Automation Framework

## Features
- Playwright browser automation (Python)
- Allure reporting
- Parallel test execution
- Modular, reusable login and utility functions
- Pytest fixtures for browser/page management

## Setup
1. Create and activate a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   playwright install
   ```

## Running Tests
- Run all tests in parallel with Allure reporting:
  ```bash
  pytest
  ```
- View Allure report:
  ```bash
  allure serve allure-results
  ```

## Project Structure
- `tests/` - All test cases and utilities
- `tests/utils.py` - Reusable helper functions (e.g., login)
- `conftest.py` - Pytest fixtures for browser/page
- `pytest.ini` - Pytest configuration (parallel, Allure, markers)

## Adding Tests
- Place new test files in `tests/`.
- Use fixtures and helpers for consistency.

## Markers
- `@pytest.mark.login` - Login tests
- `@pytest.mark.smoke` - Smoke tests

## Advanced Topics

### Data-Driven and Parametrized Testing
- Use `pytest.mark.parametrize` for running tests with multiple data sets (see BOM and Concurrency examples).
- Combine with Allure steps and attachments for detailed reporting.

### Workflow Simulation
- Simulate business workflows in tests using Allure steps and attachments (see BOM workflow simulation example).

### Concurrency and Parallelism
- Use `pytest-xdist` for parallel execution: `pytest -n auto`.
- Write tests for concurrent users, race conditions, or resource contention (see Concurrency example file).

### UI and API Test Integration
- Combine Playwright UI automation and API validation in a single test for end-to-end coverage.

### Logging and Debugging
- Use the logging utility for detailed logs in both console and file.
- Attach logs or screenshots to Allure reports for failed steps.

### CI/CD Integration (Optional)
- Integrate with CI/CD tools (GitHub Actions, GitLab CI, Jenkins) for automated test runs.
- Publish Allure reports and Slack notifications in your pipeline.

### Test Data Management (Optional)
- Store test data in YAML, JSON, or CSV files and load dynamically in tests.
- Use fixtures for setup/teardown of test data.

### Environment Configuration (Optional)
- Add a `.env` file at the project root (see `.env.example`) and set environment variables for URLs, credentials, and secrets.
- Reference environment variables in your tests and helpers using `os.environ.get()` (see BOM and Concurrency example files).
- Example:
  ```python
  import os
  BASE_URL = os.environ.get('BASE_URL', 'https://example.com')
  ```
- Do not hardcode sensitive or environment-specific data in test files.

## Moving the Framework to Git

1. **Initialize a Git repository (if not already done):**
   ```bash
   git init
   ```
2. **Add all files to the repository:**
   ```bash
   git add .
   ```
3. **Commit your changes:**
   ```bash
   git commit -m "Initial commit: Playwright Python automation framework"
   ```
4. **Create a new repository on GitHub, GitLab, or your preferred Git hosting service.**
5. **Add the remote origin (replace `<your-repo-url>` with your actual repo URL):**
   ```bash
   git remote add origin <your-repo-url>
   ```
6. **Push your code to the remote repository:**
   ```bash
   git push -u origin main
   ```
   (If your default branch is `master`, use `master` instead of `main`.)

7. **(Optional) Add a `.gitignore` file** to exclude files like `.env`, `__pycache__/`, `allure-results/`, `.venv/`, etc.

Example `.gitignore`:
```
.env
.venv/
__pycache__/
allure-results/
*.pyc
archive/
```

After these steps, your framework will be version-controlled and available on your Git hosting platform.
