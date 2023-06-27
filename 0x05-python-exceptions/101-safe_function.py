#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    result = 0
    try:
        result = fct(*args)
        return (result)
    except IndexError:
        print("Exception: list index out of range", file=sys.stderr)
    except ZeroDivisionError:
        print("Exception: division by zero", file=sys.stderr)
    return (None)
