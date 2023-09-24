#this is for testing functions in main.py

from main import check_python_version_and_os

required_version = "3.7, 3.8, 3.9, 3.11"
required_os = "Linux, Windows"

python_version_meets_requirement, os_name_matches_requirement = check_python_version_and_os(required_version, required_os)

# Assertions for testing
assert python_version_meets_requirement, f"Python version {required_version} or higher is not satisfied."
assert os_name_matches_requirement, f"OS {required_os} is not satisfied."

print("Both requirements are satisfied.")
