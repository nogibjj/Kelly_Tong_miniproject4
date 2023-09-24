from main import check_python_version_and_os

def test_check_python_version_and_os():
    required_versions = ["3.7", "3.8", "3.9", "3.11"]
    required_oses = ["Linux", "Windows"]

    for version in required_versions:
        for os_name in required_oses:
            python_version_meets_requirement, os_name_matches_requirement = check_python_version_and_os([version], [os_name])

            assert python_version_meets_requirement, f"Python version {version} or higher is not satisfied on {os_name}."
            assert os_name_matches_requirement, f"OS {os_name} is not satisfied for Python version {version}."
