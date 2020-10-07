# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 00:24:24 2020

@author: ckn32
"""

def convert(year):
    if year >= 2019:
        wareki = year - 2018
        return '令和' + str(wareki) + '年'
    elif year > 1988:
        wareki = year - 1988
        return '平成' + str(wareki) + '年'
    elif year >= 1926:
        wareki = year - 1925
        return '昭和' + str(wareki) + '年'
    elif year > 1911:
        wareki = year - 1911
        return '大正' + str(wareki) + '年'
    elif year > 1867:
        wareki = year - 1867
        return '明治' + str(wareki) + '年'
    
def judge(year):
    if (year >= 1868 or 2020 >= year):
        return True
    else:
        return False

while True:
    year = int(input('1868 ~ 2020の西暦を入力してください: '))
    if judge(year) == True:
        print(convert(year))
        break
        