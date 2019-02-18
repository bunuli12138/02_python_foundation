#!/usr/bin/env python
# encoding: utf-8
"""
@Author     :xinbei
@Software   :Pycharm
@File       :01class_instance.py
@Time       :2019/2/18 14:37
@Version    :
@Purpose    :
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
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'


def sl():
    time.sleep(0.012)
    print('sl is running')

if __name__ == '__main__':
    lisa = Student('Lisa', 99)
    bart = Student('Bart', 59)
    print(lisa.name, lisa.get_grade())
    print(bart.name, bart.get_grade())

    # python允许实例绑定不同的类定义没有的属性
    lisa.age = 18
    print(lisa.age)
    # print(bart.age) # bart不存在age属性

    # 实例绑定方法
    # from types import MethodType
    # lisa.sl = MethodType(sl, lisa)  # 给实例绑定一个方法
    # lisa.sl()
    lisa.sl = sl
    lisa.sl()
