#!/usr/bin/python3
# Fetches a URL and displays response info using urllib

from urllib import request

url = "https://intranet.hbtn.io/status"

with request.urlopen(url) as response:
    body = response.read()

print("Body response:")
print("\t- type: {}".format(type(body)))
print("\t- content: {}".format(body))
print("\t- utf8 content: {}".format(body.decode("utf-8")))
