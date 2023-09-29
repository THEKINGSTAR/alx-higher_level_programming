#!/usr/bin/python3

"""
Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and
displays the body of the response (decoded in utf-8)
The email must be sent in the email variable
You must use the packages urllib and sys
You are not allowed to import packages other than urllib and sys
You don’t need to check arguments passed to the script (number or type)
You must use the with statement
"""

import urllib.request
import urllib.parse
import sys


args = sys.argv

try:
    u_r_l = args[1]
    email = args[2]
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    with urllib.request.urlopen(url, data=data) as response:
        response_body = response.read().decode('utf-8')
        print(response_body)

except Exception as e:
    print(e)
