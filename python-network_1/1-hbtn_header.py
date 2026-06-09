#!/usr/bin/python3
# Gets X-Request-Id header value from response using urllib

import sys
from urllib import request

url = sys.argv[1]

with request.urlopen(url) as response:
    headers = response.headers
    print(headers.get("X-Request-Id"))
