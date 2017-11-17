#!/usr/bin/python
# -*- coding: utf-8 -*-

def golf(b):
    return sum([(ord(b[i])-65)*9+int(b[i+1]) for i in range(len(b)-1) if b[i].isupper() and 48<ord(b[i+1])<58])
	return sum([(ord(v)-65)*9+int(b[i+1]) for i,v in enumerate(b) if v.isupper() and 48<ord(b[i+1])<58])
# if __name__ == '__main__':
#    # These "asserts" using only for self-checking and not necessary for auto-testing
#    assert golf("ASDA1,BB22D01C1") == 31
#    assert golf("B1,C2,D3") == 60
#    print("Earn cool rewards by using the 'Check' button!")
