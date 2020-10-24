# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 03:41:47 2020

@author: ckn32
"""

def gcd(a, b):
    while a % b != 0:
        a, b = b, a % b
    return b

print(gcd(1274, 975))