#!/usr/bin/python3

"""
Python script that takes in a URL
sends a request to the URL
displays the body of the response (decoded in utf-8)
You have to manage urllib.error.HTTPError exceptions
print: Error code: followed by the HTTP status code
"""


if __name__ == "__main__":
    """
    displays the body of the response (decoded in utf-8)
    """

    import urllib.request
    import urllib.parse
    import urllib.error
    import sys

    try:
        args = sys.argv
        link = args[1]
        with urllib.request.urlopen(url=link) as response:
            response_body = response.read().decode('utf-8')
            print(response_body)

    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
