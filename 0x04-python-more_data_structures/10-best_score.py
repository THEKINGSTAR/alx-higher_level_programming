#!/usr/bin/python3
def best_score(a_dictionary):
    s_d = {}
    a_dict = a_dictionary
    if not a_dictionary:
        return None
    ###################################
    # sort_dict = {k: v for k,
    # v in sorted(a_dictionary.items(),
    # key=lambda item: item[1])}
    ###################################
    s_d = dict(sorted(a_dict.items(), reverse=True, key=lambda item: item[1]))
    res = next(iter(s_d))
    return str(res)
