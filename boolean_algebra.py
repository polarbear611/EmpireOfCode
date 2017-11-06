#!/usr/bin/python
# -*- coding: utf-8 -*-

OPERATION_NAMES = ("conjunction", "disjunction", "implication", "exclusive", "equivalence")


def boolean(x, y, operation):
    if "conjunction" == operation:
        result = x and y
    if "disjunction" == operation:
        result = x or y
    if "implication" == operation:
        result = not x or y
    if "exclusive" == operation:
        result = (x or y) and not(x and y)
    if "equivalence" == operation:
        result = x == y
    return int(result)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert boolean(1, 0, "conjunction") == 0, "and"
    assert boolean(1, 0, "disjunction") == 1, "or"
    assert boolean(1, 1, "implication") == 1, "material"
    assert boolean(0, 1, "exclusive") == 1, "xor"
    assert boolean(0, 1, "equivalence") == 0, "same?"

    print("All done? Earn rewards by using the 'Check' button!")
