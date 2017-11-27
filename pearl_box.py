#!/usr/bin/python
# -*- coding: utf-8 -*-

def p_nstep(p_sum, black, white):
    total = black + white
    return [[black * p_sum, black - 1 if black > 1 else 0, white + 1], [white * p_sum, black + 1, white - 1 if white > 1 else 0]]
    
def probability(marbles, step):
    black = marbles.count('b')
    white = marbles.count('w')
    total = black + white
    state = {0:[[1, black, white]]}
    for i in range(1, step):
        si = []
        for s in state[i - 1]:
            si += p_nstep(*s)
        state[i] = si
    #第n次总
    sn = state[step - 1]
    print(sum([s[0] * s[2] for s in sn]) / pow(total, step)) 
    return round(sum([s[0] * s[2] for s in sn]) / pow(total, step), 2)

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    def almost_equal(checked, correct, significant_digits=2):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    assert almost_equal(probability('bbw', 3), 0.48), "1st example"
    assert almost_equal(probability('wwb', 3), 0.52), "2nd example"
    assert almost_equal(probability('www', 3), 0.56), "3rd example"
    assert almost_equal(probability('bbbb', 1), 0), "4th example"
    assert almost_equal(probability('wwbb', 4), 0.5), "5th example"
    assert almost_equal(probability('bwbwbwb', 5), 0.48), "6th example"

    print("All done? Earn rewards by using the 'Check' button!")

