#!/usr/bin/python3
def magic_calculation(a, b):
    resul = 0
    for k in range(1, 3):
        try:
            if k > a:
                raise Exception('Too far')
            resul += (a ** b) / i
        except Exception:
            resul = b + a
            break
    return resul
