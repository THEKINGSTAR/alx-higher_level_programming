#!/usr/bin/python3

"""
Python script that takes in a URL,
sends a request to the URL
and
displays the body of the response (decoded in utf-8).
You have to manage urllib.error.HTTPError exceptions
and
print: Error code: followed by the HTTP status code
You must use the packages urllib and sys
You are not allowed to import other packages than urllib and sys
You don’t need to check arguments passed to the script (number or type)
You must use the with statement
"""

import urllib.request
import urllib.parse
import sys


try:
    args = sys.argv
    
    with urllib.request.urlopen(args[1]) as response:
        response_body = response.read().decode('utf-8')
        print(response_body)

except urllib.error.HTTPError as e:
    print(f"Error code: {e.code}")
