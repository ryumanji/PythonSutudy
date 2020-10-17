# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 22:26:59 2020

@author: ckn32
"""

import queue

q = queue.Queue()

q.put(3)
q.put(5)
q.put(2)

temp = q.get()
print(temp)

temp = q.get()
print(temp)

q.put(4)
temp = q.get()
print(temp)