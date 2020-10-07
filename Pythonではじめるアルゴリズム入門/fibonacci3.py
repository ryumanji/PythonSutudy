# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 22:33:49 2020

@author: ckn32
"""

memo = {1: 1, 2: 1}

def fibonacci(n):
    if n in memo:
        return memo[n]
    
    memo[n] = fibonacci(n - 2) + fibonacci(n - 1)
    return memo[n]