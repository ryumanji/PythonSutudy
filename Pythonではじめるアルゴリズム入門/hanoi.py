# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 00:43:05 2020

@author: ckn32
"""

def hanoi(n, src, dist, via):
    if n > 1:
        hanoi(n - 1, src, via, dist)
        print(src + ' -> ' + dist)
        hanoi(n - 1, via, dist, src)
    else:
        print(src + ' -> ' + dist)
        
n = int(input('円盤の枚数: '))
hanoi(n, 'a', 'b', 'c')