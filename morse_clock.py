#!/usr/bin/python
# -*- coding: utf-8 -*-

def morse_time(time_string):
    hh,mm,ss = time_string.split(":")
    if len(hh) == 1:
        hh = '0' + hh
    if len(mm) == 1:
        mm = '0' + mm
    if len(ss) == 1:
        ss = '0' + ss
    morse = ""
    two = {'0':"..", '1':".-", '2':"-."}
    three = {"0":"...", "1":"..-", "2":".-.", "3":".--", "4":"-..", "5":"-.-"}
    four = {"0":"....", "1":"...-", "2":"..-.", "3":"..--", "4":".-..", "5":".-.-", "6":".--.", "7":".---","8":'-...', "9":"-..-"}
    
    return two[hh[0]] + ' ' + four[hh[1]] + ' : ' + three[mm[0]] + ' ' + four[mm[1]] + ' : ' + three[ss[0]] + ' ' + four[ss[1]]


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert morse_time("10:37:49") == ".- .... : .-- .--- : -.. -..-", "First Test"
    assert morse_time("21:34:56") == "-. ...- : .-- .-.. : -.- .--.", "Second Test"
    assert morse_time("00:1:02") == ".. .... : ... ...- : ... ..-.", "Third Test"
    assert morse_time("23:59:59") == "-. ..-- : -.- -..- : -.- -..-", "Fourth Test"

    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

