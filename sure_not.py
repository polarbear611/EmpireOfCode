#!usr/bin/python
# -*- coding: utf-8 -*-

def sure_not(line):
    return line if line.startswith('not ') else 'not ' + line

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert sure_not("sure") == "not sure", "1st example";
    assert sure_not("not sure") == "not sure", "2st example";
    assert sure_not("noter") == "not noter", "3st example";

    print("Code's finished? Earn rewards by clicking 'Check' to review your tests!")
						
