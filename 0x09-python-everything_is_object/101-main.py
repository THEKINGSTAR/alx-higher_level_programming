#!/usr/bin/python3
LockedClass = __import__('101-locked_class').LockedClass

lc = LockedClass()
lc.first_name = "John"
try:
    lc.last_name = "Snow"
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

"""
guillaume@ubuntu:~/0x09$ ./101-main.py
[AttributeError] 'LockedClass' object has no attribute 'last_name'
guillaume@ubuntu:~/0x09$
"""
