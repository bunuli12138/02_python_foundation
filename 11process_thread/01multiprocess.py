#!/usr/bin/env python
# encoding: utf-8
"""
@Author     :xinbei
@Software   :Pycharm
@File       :01multiprocess.py
@Time       :2019/2/22 21:09
@Version    :
@Purpose    :
"""
from multiprocessing import Pool # 线程池
from multiprocessing import Process # 单个进程
import subprocess # 子进程
from multiprocessing import Queue  # 进程间通信
import os, time, random

"""单个进程"""
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid())) # 当前进程id

def single_process(func):
    print('Parent process %s.' % os.getpid())
    p = Process(target=func, args=('test',))  # 传入一个执行函数和函数的参数，创建一个Process实例
    print('Child process will start.')
    p.start()  # 启动
    p.join()
    print('Child process end.')

"""线程池"""
def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

def pool_process():
    print('Parent process %s.' % os.getpid())
    p = Pool()
    for i in range(5):
        p.apply_async(long_time_task, args=(i,)) # 异步执行的函数
    print('Waiting for all subprocesses done...')
    p.close() # 关闭进程池，不添加新的进程
    p.join()
    print('All subprocesses done.')


"""子进程"""
def ns():
    print('$ nslookup www.python.org')
    r = subprocess.call(['nslookup', 'www.python.org']) #
    print('Exit code:', r)
def ns_communicate():
    print('$ nslookup')
    p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
    print(output.decode('gbk'))
    print('Exit code:', p.returncode)


"""进程间通信"""
def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())

def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)

def queue_process():
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr.start()
    # 等待pw结束:
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()
if __name__=='__main__':
    # single_process(run_proc)
    # pool_process()
    # ns()
    # ns_communicate()
    queue_process()
    pass