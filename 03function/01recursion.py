#!/usr/bin/env python
# encoding: utf-8
"""
@Author     :xinbei
@Software   :Pycharm
@File       :01recursion.py
@Time       :2019/2/12 21:31
@Version    :
@Purpose    :使用递归函数定义简单，逻辑清晰，但需要注意防止栈溢出。可以通过通过尾递归优化
"""

import traceback

# 普通递归：
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1) # 此处引入乘法表达式，所以就不是尾递归了。

# 改成尾递归方式，主要是要把每一步的乘积传入到递归函数中。
def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)

try:
    print(fact(200))
    print(fact_iter(200,1))
except Exception as e:
    traceback.print_exc(e)