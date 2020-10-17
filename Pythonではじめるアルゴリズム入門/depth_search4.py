# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 23:10:47 2020

@author: ckn32
"""

tree = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], 
        [13, 14], [], [], [], [], [], [], [], []]

data = [0]
while len(data) > 0:
    pos = data.pop()
    print(pos, end=' ')
    for i in tree[pos]:
        data.append(i)