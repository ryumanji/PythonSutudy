# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 22:37:15 2020

@author: ckn32
"""

def fibonacci(n):
    fib = [1, 1]
    for i in range(2, n):
        fib.append(fib[i - 2] + fib[i - 1])
        
    return ifb[n - 1]