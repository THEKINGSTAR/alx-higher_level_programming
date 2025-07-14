#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    result = 0
    try:
        result = fct(*args)
        return (result)
    except IndexError as i:
        print(f"Exception: {i}", file=sys.stderr)
    except ZeroDivisionError as z:
        print(f"Exception: {z}", file=sys.stderr)
    return (None)
