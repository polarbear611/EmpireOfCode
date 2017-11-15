#!/usr/bin/python
# -*- coding: utf-8 -*-

def count_units(number):
    s = ''
    while(number):
        s += str(number % 2)
        number = int(number / 2)
        
    return s.count('1')

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_units(4) == 1
    assert count_units(15) == 4
    assert count_units(1) == 1
    assert count_units(1022) == 9

    print("Use 'Check' to earn sweet rewards!")

