#!/usr/bin/env python3
#-*- coding: gb2312 -*-

# multithread
import time, threading

# �ٶ�����������д��:
balance = 0

def change_it(n):
    # �ȴ��ȡ�����Ӧ��Ϊ0:
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(10000000):
        change_it(n)

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)
