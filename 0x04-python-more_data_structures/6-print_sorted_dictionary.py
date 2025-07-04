#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sort_dict = dict(sorted(a_dictionary.items()))
    for k in sort_dict:
        print(f"{k}: {sort_dict[k]}")
