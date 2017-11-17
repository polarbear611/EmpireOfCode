#!/usr/bin/python
# -*- coding: utf-8 -*-

def golf(d):
	s,t=0,[]
	for c in d:
		if 'U'==c[1]:t+=[int(c[5])]
		elif "POP"==c and t:s+=t.pop()
		elif t:s+=t[-1]
	return s
# if __name__ == '__main__':
#    # These "asserts" using only for self-checking and not necessary for auto-testing
#    assert golf(("PUSH 3", "POP", "POP", "PUSH 4", "PEEK", "PUSH 9", "PUSH 0", "PEEK", "POP", "PUSH 1", "PEEK")) == 8, "Example"
#    assert golf(("POP", "POP")) == 0, "PopPop"
#    assert golf(("PUSH 9", "PUSH 9", "POP")) == 9, "Push 9"
#    assert golf(()) == 0, "Empty"
#    print("All done? Earn rewards by using the 'Check' button!")
