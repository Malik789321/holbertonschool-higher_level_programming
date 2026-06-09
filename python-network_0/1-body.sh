#!/bin/bash
# Sends GET request and displays body only if status code is 200
curl -sL -w "%{http_code}" "$1" -o /tmp/body | grep -q "200" && cat /tmp/body
