#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
 define default parameters must point to invarient object: e.g. None
'''
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

L = []
add_end(L)
print(L)
L = add_end()
print(L)
L = add_end()
print(L)

s = calc(1, 2, 3)
print(s)

