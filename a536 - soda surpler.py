# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 14:20:28 2020

@author: user
"""

ans = []
for i in range(int(input())):
    e, f, c = map(int, input().split(' ') )
    e += f
    f = 0
    while e >= c:
        f += e // c
        e = (e // c) + (e % c)
    ans.append(f)    

for i in ans:
    print(i)

