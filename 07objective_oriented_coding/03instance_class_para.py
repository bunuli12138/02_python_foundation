#!/usr/bin/env python
# encoding: utf-8
"""
@Author     :xinbei
@Software   :Pycharm
@File       :03instance_class_para.py
@Time       :2019/2/18 15:49
@Version    :
@Purpose    :为了统计学生人数，可以给Student类增加一个类属性，每创建一个实例，该属性自动增加
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
    count = 0

    def __init__(self, name):
        Student.count += 1
        self.name = name


if __name__ == '__main__':
    # 测试:
    if Student.count != 0:
        print('测试失败!')
    else:
        bart = Student('Bart')
        if Student.count != 1:
            print('测试失败!')
        else:
            lisa = Student('Bart')
            if Student.count != 2:
                print('测试失败!')
            else:
                print('Students:', Student.count)
                print('测试通过!')
    print(Student.count)