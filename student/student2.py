#!/usr/bin/env python3
#-*- coding: utf-8 -*-

'''
double `__' defined private variables in python
'''

class Student(object):
    count = 0
    
    def __init__(self, name):
        self.name = name
        Student.count += 1

if Student.count != 0:
    print('test fail!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('test fail!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('test fail!')
        else:
            print('Students:', Student.count)
            print('test pass!')
