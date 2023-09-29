#!/usr/bin/python3
""" Python script that takes in a URL, sends a request to the URL """


if __name__ == "__main__":
    """
    sends a POST request to the passed URL
    with the email as a parameter
    and finally displays the body of the response.
    """

    import requests
    import sys

    try:
        args = sys.argv
        u_r_l = args[1]
        email = args[2]
        response = requests.get(sys.argv[1])
        answer = response.headers['X-Request-Id']
        print(answer)

    except Exception as e:
        print(e)
