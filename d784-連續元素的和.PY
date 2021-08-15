# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 16:07:24 2021

@author: user
"""

for j in range(int(input())):    
    list1 = list(map(int,input().split(' ')))
    a = 0
    max = -1e9
    
    for i in range(1,len(list1)):
        a += list1[i]
        if a >= max:
            max = a
           
    print(max)    