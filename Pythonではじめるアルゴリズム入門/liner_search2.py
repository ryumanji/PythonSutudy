# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 20:57:31 2020

@author: ckn32
"""

def liner_search(data, value):
    for i in range(len(data)):
        if data[i] == value:
            return i
    return -1

data = [50, 30, 90, 10, 20, 70, 60, 40, 80]
print(liner_search(data, 40))