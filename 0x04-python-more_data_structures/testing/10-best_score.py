#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    for key in a_dictionary:
        if not a_dictionary[key]:
            a_dictionary[key] = None
    sorted_dicti = dict(sorted(a_dictionary.items(), key=lambda t:t[1], reverse=True))
    best_value = next(iter(sorted_dicti))
    return best_value