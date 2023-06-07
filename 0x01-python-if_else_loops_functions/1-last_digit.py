#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
"""
The output of the program should be:
The string Last digit of, followed by
the number, followed by
the string is, followed by the last digit of number, followed by
if the last digit is greater than 5:
the string and is greater than 5
if the last digit is 0: the string and is 0
if the last digit is less than 6 and not 0:
the string and is less than 6 and not 0
followed by a new line
"""
if number >= 0:
    last_digit = (number % 10)
    if last_digit > 5:
        greater_less = "greater than 5"
    elif last_digit == 0:
        greater_less = "0"
    elif last_digit < 6 and last_digit != 0:
        greater_less = "less than 6 and not 0"
elif number < 0:
    tmp = number * -1
    last_digit = (tmp % 10) * -1
    if last_digit == 0:
        greater_less = "0"
    elif last_digit < 5:
        greater_less = "less than 6 and not 0"


print(f"Last digit of {number} is {last_digit} and is {greater_less}")


"""
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of 4205 is 5 and is less than 6 and not 0
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of -626 is -6 and is less than 6 and not 0
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of 1144 is 4 and is less than 6 and not 0
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of -9200 is 0 and is 0
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of 5247 is 7 and is greater than 5
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of -9318 is -8 and is less than 6 and not 0
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of 3369 is 9 and is greater than 5
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of -5224 is -4 and is less than 6 and not 0
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of -4485 is -5 and is less than 6 and not 0
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of 3850 is 0 and is 0
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of 5169 is 9 and is greater than 5
guillaume@ubuntu:~/0x01$
"""
