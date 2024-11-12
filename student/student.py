#!/usr/bin/env python3
#-*- coding: utf-8 -*-

class Student(object):
    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2015 - self._birth

s = Student()
s.birth = 90  #set first
print(s.birth, s.age)
