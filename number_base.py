#!/usr/bin/python
# -*- coding: utf-8 -*-

def convert(str_number, radix):
    result = 0
	rev = list(str_number[::-1])
	for i in range(len(rev)):
		if rev[i].isupper():
			rev[i] = 10 + ord(rev[i]) - ord('A')
		if int(rev[i]) >= radix:
			return -1
		result += int(rev[i]) * pow(radix, i)
	return result


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert convert("AF", 16) == 175, "Hex"
    assert convert("101", 2) == 5, "Bin"
    assert convert("101", 5) == 26, "5 base"
    assert convert("Z", 36) == 35, "Z base"
    assert convert("AB", 10) == -1, "B > A > 10"

    print("Use 'Check' to earn sweet rewards!")
