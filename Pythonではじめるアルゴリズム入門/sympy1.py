# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 22:24:29 2020

@author: ckn32
"""

from sympy import sieve

print([i for i in sieve.primerange(1, 200)])