#!/usr/bin/python3
import sys

arg_len = len(sys.argv) - 1
if arg_len == 0:
    print("0 arguments.")
elif arg_len == 1:
    print("1 argument:")
    print("{}: {}".format(arg_len, sys.argv[1]))
else:
    print("{} arguments:".format(arg_len))
    num = 1
    for arg in sys.argv[1:]:
        print("{}: {}".format(num, arg))
        num = num + 1
