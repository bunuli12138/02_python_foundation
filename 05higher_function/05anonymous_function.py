#!/usr/bin/env python
# encoding: utf-8
"""
@Author     :xinbei
@Software   :Pycharm
@File       :05anonymous_function.py
@Time       :2019/2/18 10:44
@Version    :
@Purpose    :用匿名函数改造下面的代码并
"""


# 改造is_odd
def is_odd(n):
    return n % 2 == 1
# 等效果匿名函数：
L = list(filter(lambda n:n % 2 == 1, range(1, 20)))
print(L)

# 直接修改函数
def is_odd_changed(n):
    return lambda :n % 2 == 1
print(is_odd_changed(4)) # 返回lambda函数对象
print(is_odd_changed(4)()) # 通过()才能调用返回的函数对象
