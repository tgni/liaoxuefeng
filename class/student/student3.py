#!/usr/bin/env python3
#-*- coding: utf-8 -*-

class Student(object):
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return 'Student %s' % self.name

    def __len__(self):
        return len(self.name)

    __repr__ = __str__

s = Student('Michael')

print(s, s.name, len(s))
