#!/usr/bin/python
# -*- coding: utf-8 -*-

def most_letter(text, all_letters=False):
    # replace this for solution
    d = {}
    for c in text:
        if c.isalpha():
            c = c.lower()
            if not c in d:
                d[c] = 1
            else:
                d[c] += 1
    if not all_letters:
        return sorted([k for k,v in d.items() if v == max(d.values())])[0]
    #rank3
    else:
        #put all frequencies in a list and sort by descending order
        vl = sorted(list(set(sorted(d.values()))), reverse=True)
        all = ''
        #iterate the frequency list
        for v in vl:
            lc = []
            #find same frequency letters and sort by alphabetical order
            for c, n in d.items():
                if n == v:
                    lc.append(c)
            all += ''.join(sorted(lc))
        print(all)
        return all

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    # Rank_1
    assert most_letter("Hello World!") == "l", "Hello test"
    assert most_letter("How do you do?") == "o", "O is most wanted"
    result = most_letter("One")
    assert len(result) == 1 and result in "one", "All letter only once."
    assert most_letter("Oops!") == "o", "Don't forget about lower case."
    result = most_letter("AAaooo!!!!")
    assert len(result) == 1 and result in "ao", "Only letters."
    result = most_letter("abe")
    assert len(result) == 1 and result in "abe", "The First."
    result = most_letter("Lorem ipsum dolor sit amet")
    assert len(result) == 1 and result in "mo", "Lorem 1."

    # Rank_2
    assert most_letter("Lorem ipsum dolor sit amet") == "m", "Lorem 2."
    assert most_letter("One") == "e", "One 2"
    assert most_letter("AAaooo!!!!") == "a", "Only letters. 2"
    assert most_letter("bcdefghijklmnaopqrstuvwxyz") == "a", "ABC"

    # Rank_3
    assert most_letter("Lorem ipsum dolor sit amet", True) == "moeilrstadpu", "Lorem 3."

    print("Use 'Check' to earn sweet rewards!")

