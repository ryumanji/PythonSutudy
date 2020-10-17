# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 22:05:06 2020

@author: ckn32
"""

data = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]

for i in range(1, len(data)):
    temp = data[i]
    j = i - 1
    while (j >= 0) and (data[j] > temp):
        data[j + 1] = data[j]
        j -= 1
    data[j + 1] = temp

print(data)