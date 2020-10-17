# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 12:28:01 2020

@author: ckn32
"""

def make_tree(n):
    tree = [i for i in range(n, 11)]
    inner_list = []
    inner_list.append(tree)
    print(inner_list)
    print(tree)
make_tree(1)