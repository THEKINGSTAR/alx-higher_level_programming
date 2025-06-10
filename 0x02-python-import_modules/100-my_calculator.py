#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg_len = len(sys.argv) - 1

    if arg_len != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif arg_len == 3:
        if sys.argv[2] not in ['+', '-', '/', '*']:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
    else:
        print("{} arguments:".format(arg_len))
        num = 1
        for arg in sys.argv[1:]:
            print("{}: {}".format(num, arg))
            num = num + 1

if __name__ == "__main__":
    import calculator_1 as calc

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    opp = sys.argv[2]
    if opp == '+':
        print("{} + {} = {}".format(a, b, calc.add(a, b)))
    elif opp == '-':
        print("{} - {} = {}".format(a, b, calc.sub(a, b)))
    elif opp == '*':
        print("{} * {} = {}".format(a, b, calc.mul(a, b)))
    elif opp == '/':
        print("{} / {} = {}".format(a, b, calc.div(a, b)))
