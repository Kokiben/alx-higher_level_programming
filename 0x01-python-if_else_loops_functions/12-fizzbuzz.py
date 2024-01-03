#!/usr/bin/python3
def fizzbuzz():
    for a in range(1, 101):
        if a % 3 == 0 and i % 5 == 0:
            print('FizzBuzz '.format(a), end='')
        elif a % 3 == 0:
            print('Fizz '.format(a), end='')
        elif a % 5 == 0:
            print('Buzz '.format(a), end='')
        else:
            print('{:d} '.format(a), end='')
