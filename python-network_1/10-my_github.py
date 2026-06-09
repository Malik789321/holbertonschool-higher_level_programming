#!/usr/bin/python3
"""Get GitHub user id using Basic Auth"""

import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    url = "https://api.github.com/user"

    response = requests.get(url, auth=HTTPBasicAuth(username, password))

    if response.status_code == 200:
        print(response.json().get("id"))
    else:
        print("None")
