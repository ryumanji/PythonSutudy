# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 22:30:47 2020

@author: ckn32
"""

def fibonacci(n):
    if (n == 1) or (n == 2):
        return 1
    return fibonacci(n - 2) + fibonacci(n - 1)

print(fibonacci(6))