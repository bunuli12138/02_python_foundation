#!/usr/bin/env python
# encoding: utf-8
"""
@Author     :xinbei
@Software   :Pycharm
@File       :02property_decorator.py
@Time       :2019/2/18 17:20
@Version    :
@Purpose    :用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution
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
    @property
    def score(self):
        return self._score

    @score.setter # 设置分数的方法
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value


class Screen(object):
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._heigt = value

    @property
    def resolution(self):
        return self._heigt * self._width
if __name__ == '__main__':
    s = Student()
    s.score = 80
    # s.score = 9999 # error，说明@score.setter有用
    try:
        print(s.score)
    except AttributeError as e:
        print("you did not define 'score'")

    # 测试:
    s = Screen()
    s.width = 1024
    s.height = 768
    print('resolution =', s.resolution)
    if s.resolution == 786432:
        print('测试通过!')
    else:
        print('测试失败!')