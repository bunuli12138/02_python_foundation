#!/usr/bin/env python
# encoding: utf-8
"""
@Author     :xinbei
@Software   :Pycharm
@File       :01para_slot.py
@Time       :2019/2/18 16:13
@Version    :
@Purpose    :__slots__定义的限制仅对当前类实例起作用，对继承的子类是不起作用的
"""
import functools, time


# 计算函数运行时间的装饰器
def run_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        t = time.time()
        result = func(*args, **kw)
        print('%s execute %.6f s' % (func.__name__, time.time() - t))
        return result

    return wrapper

class Student(object):
    __slots__ = ('name', 'score', 'age', 'gender', 'sl') # 可以限制绑定方法
    def __init__(self, name, score):
        self.name = name
        self.score = score

class H_stu(Student):
    pass

def sl():
    time.sleep(0.012)
    print('sl is running')

def p():
    print('pppppp')

if __name__ == '__main__':
    wy = Student('wy', 75)
    wy.sl = sl
    wy.sl()
    # wy.p = p # 无法绑定
    # wy.p()

    h = H_stu('hsn', 99)
    h.p = p  # 继承类实例可以绑定
    h.p()
    pass