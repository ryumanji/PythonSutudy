# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 22:24:10 2020

@author: ckn32
"""

stack = []

stack.append(3)
stack.append(5)
stack.append(2)

temp = stack.pop()
print(temp)

temp = stack.pop()
print(temp)

stack.append(4)

temp = stack.pop()
print(temp)