#!/usr/bin/python
# -*- coding: utf-8 -*-

FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen",
              "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty",
              "sixty", "seventy", "eighty", "ninety"]
HUNDRED = "hundred"
THOUSAND = "thousand"

def less_thousand(number):
    text = ""
    if number >= 100:
        hun = int(number / 100)
        text += FIRST_TEN[hun - 1] + " hundred"
        number = number % 100
        if hun > 0 and number > 0:
            text += " "
    if number >= 20:
        ten = int(number / 10)
        text += OTHER_TENS[ten - 2]
        number = number % 10
        if number:
            text += " " + FIRST_TEN[number - 1]
    elif number >= 10:
        text += SECOND_TEN[number - 10]
    elif number > 0:
        text += FIRST_TEN[number - 1]
    return text


def tell_number(number):
    text = ""
    number = int(number)
    if 0 == number:
        return "zero"
    if number < 0:
        text += "minus "
        number = abs(number)
    if number >= 1000:
        thousand = int(number / 1000)
        text += less_thousand(thousand) + " thousand"
        number = number % 1000
        if thousand and number:
            text += " "
        if not number:
            return text
    text += less_thousand(number)
    print(text)
    return text

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    # Rank 1
    assert tell_number(4) == 'four', "1st example"
    assert tell_number(133) == 'one hundred thirty three', "2nd example"
    assert tell_number(12) == 'twelve', "3rd example"
    assert tell_number(101) == 'one hundred one', "4th example"
    assert tell_number(212) == 'two hundred twelve', "5th example"
    assert tell_number(40) == 'forty', "6th example"
    assert not tell_number(212).endswith(' '), "Dont forget strip whitespaces at the end of string"

    # Rank 2
    assert tell_number(-133) == 'minus one hundred thirty three', "Minus"
    assert tell_number(0) == 'zero', "Zero"

    # Rank 3
    assert tell_number(42000) == 'forty two thousand', "42 many"
    assert (tell_number(-999999) ==
            "minus nine hundred ninety nine thousand nine hundred ninety nine"), "Abyss"

    print("Earn cool rewards by using the 'Check' button!")
