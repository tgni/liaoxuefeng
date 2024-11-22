#!/usr/bin/env python3
#-*- coding: gb2312 -*-

import threading
    
# ����ȫ��ThreadLocal����:
local_school = threading.local()

def process_student():
    # ��ȡ��ǰ�̹߳�����student:
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))

def process_thread(name):
    # ��ThreadLocal��student:
    local_school.student = name
    print(local_school.student);
    process_student()

t1 = threading.Thread(target= process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target= process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()
