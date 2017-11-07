#!/usr/bin/python
# -*- coding: utf-8 -*-

from math import pi
def simple_areas(*args):
    if 1 == len(args):
        return args[0] * args[0] * pi / 4
    if 2 == len(args):
        return args[0] * args[1]
    if 3 == len(args):
        s = sum(args) / 2
        return pow(s * (s - args[0]) * (s - args[1]) * (s - args[2]), 0.5)
    

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    def almost_equal(checked, correct, significant_digits=2):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    assert almost_equal(simple_areas(3), 7.07), "Circle"
    assert almost_equal(simple_areas(2, 2), 4), "Square"
    assert almost_equal(simple_areas(2, 3), 6), "Rectangle"
    assert almost_equal(simple_areas(3, 5, 4), 6), "Triangle"
    assert almost_equal(simple_areas(1.5, 2.5, 2), 1.5), "Small triangle"

    print("Earn cool rewards by using the 'Check' button!")

