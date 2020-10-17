# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 02:47:52 2020

@author: ckn32
"""
import functools

M, N = 6, 5

# pythonでは以下の1行を追加するだけで再帰処理をメモ化できる
@functools.lru_cache(maxsize = None)
def search(m, n):
    if (m == 0) or (n == 0):
        return 1
    
    return search(m - 1, n) + search(m, n - 1)
        
print(route[M][N])
    