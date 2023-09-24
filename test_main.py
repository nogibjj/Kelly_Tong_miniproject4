from main import check_python_version_and_os

def test_check_python_version_and_os():
  required_versions = ["3.7", "3.8", "3.9", "3.11"]
  required_oses = ["Linux", "Windows"]
  
  for version in required_versions:
      for os_name in required_oses:
          python_version_meets_requirement, os_name_matches_requirement = check_python_version_and_os(version, os_name)
  
          # Assertions for testing
          assert python_version_meets_requirement == True
          assert os_name_matches_requirement == True

