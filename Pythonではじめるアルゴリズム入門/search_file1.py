# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 02:44:49 2020

@author: ckn32
"""

# PermissionError: [WinError 5] アクセスが拒否されました。: '/$Recycle.Bin/S-1-5-18/'


import os

def search(dir, name):
    for i in os.listdir(dir):
        if i == name:
            print(dir + i)
        if os.path.isdir(dir + i):
            if os.access(dir + i, os.R_OK):
                search(dir + i + '/', name)
                
search('/', 'Users')