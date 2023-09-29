#!/usr/bin/python3
"""
Python script that takes in a URL and an email address
sends a POST request to the passed URL
"""


if __name__ == "__main__":
    """
    The email must be sent in the variable email
    You must use the packages requests and sys
    You are not allowed to import packages other than requests and sys
    """

    import requests
    import sys

    try:
        args = sys.argv
        u_r_l = args[1]
        email = args[2]
        data = {'email': email}
        response = requests.post(url=u_r_l, data=data)
        print(response.text)

    except Exception as e:
        print(e)
