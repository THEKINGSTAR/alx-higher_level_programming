#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL
and displays the value of the variable X-Request-Id in the response header
"""

import requests
import sys

response = requests.get(sys.argv[1])
answer = response.headers['X-Request-Id']
print(answer)
