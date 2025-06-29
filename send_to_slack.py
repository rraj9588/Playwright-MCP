import re
import requests

# Read the pytest result file
def send_pytest_results_to_slack(result_file="result.txt", webhook_url=None, aut_name="DEMO_APP"):
    try:
        with open(result_file) as f:
            result = f.read()
    except Exception as e:
        print(f"Error reading result file: {e}")
        return

    print("Raw pytest result:\n", result)

    # Parse the number of passed and failed tests
    passed = re.search(r"=+ (\d+) passed", result)
    failed = re.search(r"=+ (\d+) failed", result)

    pass_count = int(passed.group(1)) if passed else 0
    fail_count = int(failed.group(1)) if failed else 0
    total_count = pass_count + fail_count

    print(f"Parsed: {pass_count} passed, {fail_count} failed, {total_count} total")

    # Prepare a more presentable Slack message
    message = (
        f":rocket: *Test Results*\n"
        f"-----------------------------------\n"
        f"*AUT:* `{aut_name}`\n\n"
        f"*Total Tests:* *{total_count}*\n\n"
        f":white_check_mark: *Passed:* *{pass_count}*\n"
        f":x: *Failed:* *{fail_count}*"
    )

    if webhook_url is None:
        print("Slack webhook URL must be provided.")
        return
    payload = {"text": message}
    try:
        response = requests.post(webhook_url, json=payload)
        print(f"Slack response code: {response.status_code}")
        print(f"Slack response text: {response.text}")
        if response.status_code == 200:
            print("Result sent to Slack successfully!")
        else:
            print(f"Failed to send result to Slack: {response.text}")
    except Exception as e:
        print(f"Error sending to Slack: {e}")

if __name__ == "__main__":
    # Replace with your actual Slack webhook URL
    webhook_url = "https://hooks.slack.com/services/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"
    send_pytest_results_to_slack(result_file="result.txt", webhook_url=webhook_url, aut_name="DEMO_APP")
