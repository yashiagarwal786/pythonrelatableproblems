# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 20:06:03 2020

@author: DELL
"""

### PROBLEM STATEMENT-----> ####
####   WRITE A PYTHON PROGRAM TO FIND THE GREATEST COMMMON DIVISOR(GCD) OF TWO INTEGERS

def recurgcd(a,b):
    low=min(a,b)
    high=max(a,b)
    
    if low==0:
        return high
    elif low==1:
        return 1
    else:
        return recurgcd(low , high%low)
print(recurgcd(12, 16))
