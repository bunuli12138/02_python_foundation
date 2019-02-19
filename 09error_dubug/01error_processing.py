#!/usr/bin/env python
# encoding: utf-8
"""
@Author     :xinbei
@Software   :Pycharm
@File       :01error_processing.py
@Time       :2019/2/19 12:17
@Version    :
@Purpose    :
"""

import logging # 记录错误信息
from functools import reduce
"""
可以跨越多层调用
"""
def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        print('Error:', e)
        # logging.exception(e) # 返回异常栈信息但不会终止程序
    finally:
        print('finally...')



"""
根据需要，可以定义一个错误的class，选择好继承关系，然后，用raise语句抛出一个错误的实例
"""
class FooError(ValueError):
    pass

def foo2(s):
    n = int(s)
    if n==0:
        raise FooError('invalid value: %s' % s)
    return 10 / n


"""
练习
"""
def str2num(s):
    try:
        return int(s)
    except ValueError:
        return float(s)

def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main_test():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)

if __name__ == '__main__':
    # main()
    # print('END')

    # foo2('0')

    main_test()
