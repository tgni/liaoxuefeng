#!/usr/bin/env python3
#-*- coding: utf-8 -*-

class Student(object):
    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        #self.birth = value #error: recusive invoke more than 999 times.
        self._birth = value

    @property
    def age(self):
        return 2015 - self._birth

s = Student()
s.birth = 90  #set first
print(s.birth, s.age)
#s.age = 400 #AttributeError: can't set attribute 'age'

"""
class Student(object):
    def __init__(self, name, gender):
        self.__name = name
        self.__gender = gender

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        self.__gender = gender

bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('test failed!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('test failed!')
    else:
        print('test ok')
"""
