#!/usr/bin/python3
"""Gets X-Request-Id header using requests"""

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)

    print(response.headers.get("X-Request-Id"))
