# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 21:57:06 2020

@author: ckn32
"""

import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True