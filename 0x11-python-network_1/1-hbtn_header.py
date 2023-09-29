#!/usr/bin/python3

"""
Python script that takes in a URL,
sends a request to the URL and displays the value
of the X-Request-Id variable
found in the header of the response.
"""

import urllib.request
import sys


args = sys.argv
try:
    with urllib.request.urlopen(args[1]) as response:
        if 'X-Request-Id' in response.headers:
            x_request_id = response.headers['X-Request-Id']
            print(x_request_id)
except Exception as e:
    print(e)
