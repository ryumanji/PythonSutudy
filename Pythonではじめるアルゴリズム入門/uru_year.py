# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 22:39:13 2020

@author: ckn32
"""

for i in range(1950, 2051):
    print(str(i) + '年')
    if (i % 4 == 0):
        print('うるう年')
    elif (i % 100 == 0) and (i % 400 != 0):
        print('うるう年ではない')
    else:
        print('うるう年ではない')
    