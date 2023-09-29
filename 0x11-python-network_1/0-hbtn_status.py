#!/usr/bin/python3
""" Python script that fetches https://alx-intranet.hbtn.io/status """

import urllib.request


with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    html = response.read()
print("Body response:")
print("\t- content:", type(html))
print("\t- content:", html)
print("\t- utf8 content:", html.decode('utf-8'))
