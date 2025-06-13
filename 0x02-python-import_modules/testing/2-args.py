#!/usr/bin/python3
import sys
if (len(sys.argv) - 1 == 0 ):
    print(f"0 arguments.")

if (len(sys.argv) -1  == 1):
    print("1 argument.")
    print("1: {}".format(sys.argv[1])
          )
if (len(sys.argv) -1 > 1):
    print(f"{len(sys.argv) - 1} arguments:")
    for i, arg in enumerate(sys.argv[1:]):
        print(f"{i + 1}: {arg}")
