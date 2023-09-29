#!/usr/bin/python3
""" Python script that takes in a URL, sends a request to the URL """


if __name__ == "__main__":
    """
    sends a request to the URL
    and
    displays the value of the variable X-Request-Id in the response header
    """

    import requests
    import sys

    args = sys.argv[1]
    response = requests.get(args[1])
    answer = response.headers['X-Request-Id']
    print(answer)
