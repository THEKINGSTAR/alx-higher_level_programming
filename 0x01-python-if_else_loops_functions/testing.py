#!/usr/bin/python3
for i in range(99):
    print(f"{i} = {hex(i)}")

for i in range(99):
    print(f"{i:02d}, ",  end="")
print("99")

print("")

for i in range(30):
    print("{:02d}, ".format(i), end="")
print("")
