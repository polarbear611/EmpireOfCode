#!/usr/bin/python
# -*- coding: utf-8 -*-

def cal_num_by_radix(list_n, base):
    result = 0
    list_n = list_n[::-1]
    return sum([list_n[i] * pow(base, i) for i in range(len(list_n))])

def str_to_list_number(str_number):
    return [ord(c) - ord('A') + 10 if c.isupper() else int(c) for c in str_number]
def good_radix(str_number):
    #convert to str to a number list like [10, 2, 3, 11]
    list_num = str_to_list_number(str_number)
    #find the min base
    min_radix = max(list_num) + 1
    #try to find a radix 'k' that the number is divisible by 'k - 1' without reminder
    for r in range(min_radix, 37):
        if not cal_num_by_radix(list_num, r) % (r - 1):
            return r
    return 0


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert good_radix("18") == 10, "Simple decimal"
    assert good_radix("1010101011") == 2, "Any number is divisible by 1"
    assert good_radix("222") == 3, "3rd test"
    assert good_radix("A23B") == 14, "It's not a hex"
    assert good_radix("IDDQD") == 0, "k is not exist"


    print("Now that you're finished, hit the 'Check' button to review your code and earn sweet rewards!")

