#!usr/bin/python
# -*- coding: utf-8 -*-

def golf(password):
    if len(password) < 10:
        return False
    if not password.isalnum():
        return False
    flag_lower = False
    flag_upper = False
    flag_number = False
    for c in password:
        if c.islower():
            flag_lower = True
        if c.isupper():
            flag_upper = True
        if c.isdigit():
            flag_number = True
    
    if flag_lower and flag_upper and flag_number:
        return True
    else:
        return False


