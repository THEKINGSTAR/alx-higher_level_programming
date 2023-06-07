#!/usr/bin/python3
for alpha in range(97, 97+26):
    if alpha == 97+4 or alpha == 97+16:
        continue
    print("{}".format(chr(alpha)), end="")
