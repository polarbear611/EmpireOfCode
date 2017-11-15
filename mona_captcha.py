#!/usr/bin/python
# -*- coding: utf-8 -*-

FONT = ("--X--XXX-XXX-X-X-XXX--XX-XXX-XXX--XX-XX--"
        "-XX----X---X-X-X-X---X-----X-X-X-X-X-X-X-"
        "--X---XX--X--XXX-XX--XXX--X--XXX-XXX-X-X-"
        "--X--X-----X---X---X-X-X-X---X-X---X-X-X-"
        "--X--XXX-XXX---X-XX---XX-X---XXX-XX---XX-")

def one_pixel(digit, image):
    diff = 0
    for i in range(len(digit)):
        if digit[i] != image[i]:
            diff += 1
    return diff <= 1

def recognize(image):
    fonts = [FONT[i:i+41] for i in range(0, len(FONT), 41)]
    digits = {}
    for i in range(0, len(fonts[0]) - 4, 4):
        number = []
        for j in range(5):
            number += fonts[j][i+1 : i+4]
        digits[int((i/4 + 1) % 10)] = ''.join(number)
    #print(digits)
    for i in range(5):
        for j in range(len(image[0])):
            image[i][j] = 'X' if image[i][j] == 1 else  '-'
    
    numbers = ''
    for i in range(0, len(image[0]) - 4, 4):
        number = []
        for j in range(5):
            number += image[j][i+1 : i+4]
        number = ''.join(number)
        for key, val in digits.items():
            if one_pixel(val, number):
                numbers += str(key)
    return int(numbers)
    #return 1

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert recognize([[0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0],
                    [0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                    [0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0],
                    [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0],
                    [0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0]]) == 394, "394 clear"
    assert recognize([[0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0],
                    [0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                    [0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0],
                    [0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0],
                    [0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0]]) == 394, "again 394 but with noise"

    print("Earn cool rewards by using the 'Check' button!")

