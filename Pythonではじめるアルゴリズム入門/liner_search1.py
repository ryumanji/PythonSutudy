# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 20:54:18 2020

@author: ckn32
"""

data = [50, 30, 90, 10, 20, 70, 60, 40, 80]

found = False
for i in range(len(data)):
    if data[i]== 40:
        print(i)
        found = True
        break
if not found:
    print('Not Found')