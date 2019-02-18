#!/usr/bin/env python
# encoding: utf-8
"""
@Author     :xinbei
@Software   :Pycharm
@File       :06decorator.py
@Time       :2019/2/18 12:58
@Version    :
@Purpose    :设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间
"""

import time, functools

# 构造无参数装饰器
def log_exc(func):
    def wrapped(*args, **kw):
        result = func(*args, **kw)  # 函数运行
        print('call %s():' % func.__name__)
        return result
    return wrapped
@log_exc # 相当于： now1 = log_exc(now1)
def now1():
    print('2015-3-25')


# 构造有参数装饰器
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            result = func(*args, **kw)  # 函数运行
            print('%s %s():' % (text, func.__name__))
            return result
        return wrapper
    return decorator
@log('executing') # 相当于： now2 = log('execute')(now2)
def now2():
    print('2015-3-25')

# __name__属性复制到返回函数中
def log2(func):
    @functools.wraps(func) # # 把原始函数的__name__等属性复制到wrapper()函数
    def wrapper(*args, **kw):
        result = func(*args, **kw)  # 函数运行
        print('call %s():' % func.__name__)
        return result
    return wrapper
@log2
def now3():
    print('2015-3-25')
# print(now3.__name__) # wrapper


# 练习
def metric(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        t1 = time.time()
        result = func(*args, **kw)  # 函数运行
        print('%s excute in %.6f s' % (func.__name__, time.time() - t1))
        return result
    return wrapper

@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y


@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z

if __name__ == '__main__':
    # now1()
    # now2()
    # now3()

    # 测试
    f = fast(11, 22)
    s = slow(11, 22, 33)
    print(f, s)
    if f != 33:
        print('测试失败!')
    elif s != 7986:
        print('测试失败!')