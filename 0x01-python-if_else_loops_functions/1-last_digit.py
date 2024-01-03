#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    mod = number % 10
else:
    mod = ((number * -1) % 10) * -1

mes = "Last digit of %d is %d and is" % (number, mod)

if mod == 0:
    print(mes, "0")
elif mod > 5:
    print(mes, "greater than 5")
else:
    print(mes, "less than 6 and not 0")
