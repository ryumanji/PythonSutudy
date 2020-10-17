# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 21:49:00 2020

@author: ckn32
"""

data = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]

min = 0
for i in range(1, len(data)):
    if data[min] > data[i]:
        min = i
        
print(min)