# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 21:28:53 2020

@author: ckn32
"""

n = '10010'

result = 0
for i in range(len(n)):
    result += int(n[i]) * (2 ** (len(n) - i - 1))
    
print(result)