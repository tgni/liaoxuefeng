#!/usr/bin/env python3
#-*- coding: gb2312 -*-

from multiprocessing import Process
import os, time

# 子进程要执行的代码
def run_proc(name):
    while True:
        print('Child process %s (%s) is running' % (name, os.getpid()))
        time.sleep(1)

def run_proc2(name):
    while True:
        print('Child process %s (%s) is running' % (name, os.getpid()))
        time.sleep(2)

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start()

    p2 = Process(target=run_proc2, args=('test2',))
    print('Child2 process will start.')
    p2.start()

    p.join()
    print('Child process end.')
    p2.join()
    print('Child2 process end.')
