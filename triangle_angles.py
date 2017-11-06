#!/usr/bin/python
# -*- coding: utf-8 -*-

from math import pi, acos

def angles(a, b, c):
    a, b, c = sorted([a, b, c])
    if a + b <= c :
        return [0, 0, 0]
    
    angle_c = round(acos((a * a + b * b - c * c ) / (2 * a * b)) / pi * 180)
    angle_b = round(acos((a * a + c * c - b * b ) / (2 * a * c)) / pi * 180)
    angle_a = 180 - angle_c - angle_b
    
    return [angle_a, angle_b, angle_c]
if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert angles(4, 4, 4) == [60, 60, 60], "All sides are equal"
    assert angles(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    assert angles(2, 2, 5) == [0, 0, 0], "It can not be a triangle"

    print("Code's finished? Earn rewards by clicking 'Check' to review your tests!")

