#!/usr/bin/python3
"""
Python script that takes in a URL and an email address
sends a POST request to the passed URL
"""


if __name__ == "__main__":
    """
    If the HTTP status code is greater than or equal to 400,
    print: Error code: followed by the value of the HTTP status code
    You must use the packages requests and sys
    You are not allowed to import packages other than requests and sys
    """

    import requests
    import sys

    args = sys.argv
    u_r_l = args[1]
    response = requests.get(url=u_r_l)
    er = response.status_code
    if er >= 400:
        print("Error code: {}".format(er))
    else:
        print(response.text)
