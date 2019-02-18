#!/usr/bin/env python
# encoding: utf-8
"""
@Author     :xinbei
@Software   :Pycharm
@File       :07patical_function.py
@Time       :2019/2/18 13:39
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

# 偏函数可以使参数需求大的函数固定部分参数，代码简洁以及复用
int2 = functools.partial(int, base=2) # 相当于： kw = { 'base': 2 } int('10010', **kw)
max2 = functools.partial(max, 10) # 会把10作为*args的一部分自动加到左边

if __name__ == '__main__':
    print(int2('10010'))
    print(max2(5, 6, 7)) # 相当于 max(10, 5, 6, 7)
    pass