#!/usr/bin/python3
# -*- coding: utf-8 -*-

import time, functools

def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        start_time = time.time()
        fn(*args, **kw)
        end_time = time.time()
        print('%s executed in %.3f ms' % (fn.__name__, (end_time - start_time) * 1000))
    return wrapper

#test
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('test ok!')
elif s != 7986:
    print('test fail!')
