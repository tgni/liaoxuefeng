#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def findMinAndMax(L):
    #if L == None or len(L) == 0:
    if L == []:
        return (None, None)

    return (min(L), max(L))

if findMinAndMax([]) != (None, None):
    print('fail!')
elif findMinAndMax([7]) != (7, 7):
    print('fail!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('fail!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('fail!')
else:
    print('success!')
