from main import check_python_version_and_os

def test_check_python_version_and_os():
    required_versions = ["3.7", "3.8", "3.9", "3.11"]
    required_oses = ["Linux", "Windows"]

    assert check_python_version_and_os(required_versions, required_oses) == True
