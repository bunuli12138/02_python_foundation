#!/usr/bin/env python
# encoding: utf-8
"""
@Author     :xinbei
@Software   :Pycharm
@File       :02acess_restriction.py
@Time       :2019/2/18 14:59
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


# 运行提醒
def run_mes(cla):
    @functools.wraps(cla)
    def wrapper(*args, **kw):
        result = cla(*args, **kw)
        print('%s is running...' % cla.__name__)
        return result
    return wrapper


@run_mes # 装饰器可以用于类
class Student(object):
    def __init__(self, name, score, gender):
        self.__name = name
        self.__score = score
        self.gender = gender

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

    def get_gender(self):
        return self.gender

    def set_gender(self, gender):
        self.gender = gender


if __name__ == '__main__':
    wy = Student('wy', 75, 'male')
    print(wy.get_name())

    print(hasattr(wy, 'gender'))
    print(getattr(wy, 'name', 404))
    print(getattr(wy, 'set_gender'))
    # wy._Student__name = 'hsn' # 私有变量依然可能被修改
    # print(wy.get_name())

    # 测试gender的两个方法
    bart = Student('Bart', 99, 'male')
    if bart.get_gender() != 'male':
        print('测试失败!')
    else:
        bart.set_gender('female')
        if bart.get_gender() != 'female':
            print('测试失败!')
        else:
            print('测试成功!')

