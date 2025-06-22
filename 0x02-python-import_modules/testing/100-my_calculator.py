#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    if (len(sys.argv) -1 < 3):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    elif (sys.argv[2] not in ['+', '-', '*', '/']):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    else:
        op = sys.argv[2]
        a = int(sys.argv[1])
        b = int(sys.argv[3])

        if(op == '+'):
            res = (add(a, b))
        if(op == '-'):
            res = (sub(a, b))
        if(op == '*'):
            res = (mul(a, b))
        if(op == '/'):
            res = (div(a, b))
        print(f"{a} {op} {b} = {res}")
