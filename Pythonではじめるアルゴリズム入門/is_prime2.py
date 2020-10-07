# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 22:05:32 2020

@author: ckn32
"""

import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n% i == 0:
            return False
    return True

for i in range(200):
    if is_prime(i):
        print(i, end=' ')