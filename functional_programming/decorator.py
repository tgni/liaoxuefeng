#!/usr/bin/python3
# -*- coding: utf-8 -*-

import functools

def now():
    print('2024-11-18')

'''
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

n = log(now)
n()
'''
def log(text):
    def decorator(func):
        @functools.wraps(func)  #makes n.__name__ the same as 'func', not wrapper
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

n = log('execute')(now)
n()

print(now.__name__)
print(n.__name__)

