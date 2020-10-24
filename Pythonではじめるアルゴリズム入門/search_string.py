# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 03:11:52 2020

@author: ckn32
"""

text = list('SHOEISHA SESHOP')
pattern = list('SHA')

for i in range(len(text)):
    match = True
    for j in range(len(pattern)):
        if text[i + j] != pattern[j]:
            match = False
            break
    if match:
        print(i)
        break