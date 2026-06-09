#!/usr/bin/python3
"""Sends a POST request with email parameter using urllib"""

import sys
from urllib import request, parse

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = parse.urlencode({"email": email}).encode("utf-8")
    req = request.Request(url, data=data)

    with request.urlopen(req) as response:
        print(response.read().decode("utf-8"))
