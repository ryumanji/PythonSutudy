# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 22:18:29 2020

@author: ckn32
"""

data = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]

change = True
for i in range(len(data)):
    if not change:
        break
    change = False
    for j in range(len(data) - i - 1):
        if data[j] > data[j + 1]:
            data[j], data[j + 1] = data[j + 1], data[j]
            change = True

print(data)