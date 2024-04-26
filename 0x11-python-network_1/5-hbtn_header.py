#!/usr/bin/python3
"""
Sending a request to the URL and displaying the value of the variable X-Request-Id
in the response header"""

if __name__ == '__main__':
    from requests import get
    from sys import argv

    res = get(argv[1])
    print(res.headers.get('X-Request-Id'))
