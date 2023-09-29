#!/usr/bin/python3
""" Python script that fetches https://alx-intranet.hbtn.io/status """

import urllib.request


with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    html = response.read()
print("Body response:")
print("\t- type:", type(html))
print("\t- content:", html.decode('utf-8'))
