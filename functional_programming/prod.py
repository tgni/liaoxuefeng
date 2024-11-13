#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from functools import reduce

'''
def prod(L):
    def fn(x, y):
        return x*y

    return reduce(fn,L)
'''

def prod(L):
    return reduce(lambda x,y : x*y, L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('test ok!')
else:
    print('test fail!')
