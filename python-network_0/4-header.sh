#!/bin/bash
# Sends GET request with custom header X-School-User-Id:98 and displays response body
curl -s -H "X-School-User-Id: 98" "$1"
