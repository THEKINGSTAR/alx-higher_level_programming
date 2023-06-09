#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg_len = len(sys.argv) - 1

    if arg_len == 0:
        print("0")
    else:
        sum = 0
        for arg in sys.argv[1:]:
            sum = sum + int(arg)
        print(sum)
