#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    ky_to_delet = set()
    for ky, val in a_dictionary.items():
        if val == value:
            ky_to_delet.add(ky)

    for ky in ky_to_delet:
        del a_dictionary[ky]
    return a_dictionary
