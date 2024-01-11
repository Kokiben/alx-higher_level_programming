#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_diccti = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    n = 0

    if roman_string is None or type(roman_string) is not str:
        return 0

    for a in range(len(roman_string)):
        if a == len(roman_string) - 1:
            n += roman_diccti[roman_string[a]]
        elif roman_diccti[roman_string[a]] >= roman_dicc[roman_string[a + 1]]:
            n += roman_diccti[roman_string[a]]
        else:
            n -= roman_diccti[roman_string[a]]
    return n
