#!/usr/bin/env python3
#-*- coding: gb2312 -*-

class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # ��ʼ��2��������a, b

    def __iter__(self):
        return self # ʵ��������ǵ������󣬹ʷ����Լ�

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # ������һ��ֵ
        if self.a > 100000: # �˳�ѭ��������
            raise StopIteration()
        return self.a # ������һ��ֵ

    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a
