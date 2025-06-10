#!/usr/bin/python3
import random
number = random.randint(-10, 10)
"""
The output of the program should be:
The number, followed by
if the number is greater than 0: is positive
if the number is 0: is zero
if the number is less than 0: is negative
"""
if number > 0:
    message = "is positive"
elif number == 0:
    message = "is zero"
elif number < 0:
    message = "is negative"

print(f"{number} {message}")
