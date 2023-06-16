#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    u_set = set_1.union(set_2)
    for u in (set_1.intersection(set_2)):
        u_set.remove(u)
    return (u_set)
