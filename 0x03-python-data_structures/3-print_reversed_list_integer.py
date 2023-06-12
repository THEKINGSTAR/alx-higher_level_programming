#!/usr/bin/python3
# if __name__ == "__main__":
def print_reversed_list_integer(my_list=[]):
    if my_list is None or len(my_list) == 0:
        return None
    my_list.reverse()
    for i in my_list:
        print("{:d}".format(i))
