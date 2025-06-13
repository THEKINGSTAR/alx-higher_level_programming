#!/usr/bin/python3
import hidden_4.pyc
names =  dir(hidden_4.pyc)
for name in names:
    if(name[:2] != "__"):
        print(name)
