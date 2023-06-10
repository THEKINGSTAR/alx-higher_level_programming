#!/usr/bin/python3
# Returns True if c is lowercase
# Returns False otherwise
def islower(c):
    if (ord(c) > 64) and (ord(c) < 91):
        return (False)
    if (ord(c) > 96) and (ord(c) < 123):
        return (True)
