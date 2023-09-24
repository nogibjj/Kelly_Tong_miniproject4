import os
import sys
import re

def check_python_version_and_os(required_version, required_os):
    python_version = re.search(r"\d+\.\d+", sys.version).group()
    os_name = os.getenv("RUNNER_OS")

    python_version_meets_requirement = python_version == required_version
    os_name_matches_requirement = os_name == required_os

    return python_version_meets_requirement, os_name_matches_requirement
