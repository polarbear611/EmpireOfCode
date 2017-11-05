#!/usr/bin/python
# -*- coding: utf-8 -*-

def count_words(text, words):
    count = 0
    text_words = text.split(' ')
    dict_words = {}
    for w in words:
        dict_words[w] = 0
    for t in text_words:
        for w in words:
            if t.lower().find(w) >= 0:
                dict_words[w] += 1
    for d in dict_words:
        if dict_words[d] > 0:
            count += 1
    return count


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}) == 3, "Example"
    assert count_words("Bananas, give me bananas!!!", {"banana", "bananas"}) == 2, "BANANAS!"
    assert count_words("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
                       {"sum", "hamlet", "infinity", "anything"}) == 1, "Weird text"

    print("All set? Click 'Check' to review your code and earn rewards!")
