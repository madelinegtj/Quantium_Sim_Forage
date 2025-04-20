#!/bin/bash

# Automate the test suite

# Exit on any error
set -e

# Activate the virtual environment
source quantiumsim_venv/Scripts/activate

# Run pytest
echo "Running test suite..."
pytest test_dash_app.py

# Capture pytest exit code
exit_code=$?

# Exit with the same code as pytest (0 = success, 1 = failure)
if [ $exit_code -eq 0 ]; then
    echo "All tests passed."
    exit 0
else
    echo " Some tests failed."
    exit 1
fi