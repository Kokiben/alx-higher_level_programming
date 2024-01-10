#!/usr/bin/python3
def best_score(a_dictionary):
    """return key with biggest int v"""
    if not a_dictionary:
        return None
    return max(a_dictionary, key=a_dictionary.get)
