import os
import sys
import re

def check_python_version_and_os(required_versions, required_oses):
    python_version = re.search(r"\d+\.\d+", sys.version).group()
    os_name = os.getenv("RUNNER_OS")

    if python_version in required_versions and os_name in required_oses:
        return True
