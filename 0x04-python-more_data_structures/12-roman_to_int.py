#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0

    roman_int = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    deci = 0
    previ_val = 0

    for num in reversed(roman_string):
        val = roman_int.get(num, 0)
        if val == 0:
            return 0
        if val < previ_val:
            deci -= val
        else:
            deci += val
        previ_val = val
   return deci
