#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from functools import reduce

def str2float(s):
    dot_idx = s.index('.')
    s = s.replace('.', '')
    n = list(map(int, s))

    integer_part = reduce(lambda x,y : x*10+y, n)
    return integer_part / (10 ** (len(s) - dot_idx))

print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('test ok!')
else:
    print('test fail!')
