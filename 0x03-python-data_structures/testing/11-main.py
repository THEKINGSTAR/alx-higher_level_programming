#!/usr/bin/python3
delete_at = __import__('11-delete_at').delete_at

my_list = [1, 2, 3, 4, 5]
idx = 3
new_list = delete_at(my_list, idx)
print(f"new_list: {new_list}, idx:{idx}")
print(f"my_list : {my_list} , idx:{idx}")


my_list = [1, 2, 3, 4, 5]
idx = 11
new_list = delete_at(my_list, idx)
print(f"new_list: {new_list}, idx:{idx}")
print(f"my_list : {my_list} , idx:{idx}")


my_list = []
idx = 3
new_list = delete_at(my_list, idx)
print(f"new_list: {new_list}, idx:{idx}")
print(f"my_list : {my_list} , idx:{idx}")
