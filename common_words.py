#!/usr/bin/python
# -*- coding: utf-8 -*-

def common_words(first, second):
    result = []
    first = sorted(first.split(','))
    second = sorted(second.split(','))
    for wf in first:
        for ws in second:
            if wf == ws:
                result.append(wf)
    
    return ','.join(result)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert common_words("hello,world", "hello,earth") == "hello", "Hello"
    assert common_words("one,two,three", "four,five,six") == "", "Too different"
    assert common_words("one,two,three", "four,five,one,two,six,three") == "one,three,two", "1 2 3"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

