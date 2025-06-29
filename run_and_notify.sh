#!/bin/bash
# Run all tests, save output, and send results to Slack

# Activate virtual environment if needed
test -d .venv && source .venv/bin/activate

pytest > result.txt
python send_to_slack.py
