#!/usr/bin/env python3
#-*- coding: gb2312 -*-

from multiprocessing import Process, Queue
import os, time, random

# д���ݽ���ִ�еĴ���:
def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())

# �����ݽ���ִ�еĴ���:
def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)

if __name__=='__main__':
    # �����̴���Queue�������������ӽ��̣�
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # �����ӽ���pw��д��:
    pw.start()
    # �����ӽ���pr����ȡ:
    pr.start()
    # �ȴ�pw����:
    pw.join()
    print('write process end');
    # pr����������ѭ�����޷��ȴ��������ֻ��ǿ����ֹ:
    pr.terminate()
    print('read process end');
