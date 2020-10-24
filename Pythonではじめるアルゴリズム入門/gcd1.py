# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 03:40:08 2020

@author: ckn32
"""

def gcd(a, b):
    r = a % b
    while r != 0:
        a, b = b, r
        r = a % b
        
    return b

print(gcd(1274, 975))