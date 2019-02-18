#!/usr/bin/env python
# encoding: utf-8
"""
@Author     :xinbei
@Software   :Pycharm
@File       :03sorted.py
@Time       :2019/2/16 14:29
@Version    :
@Purpose    :用sorted()对列表分别按名字排序,再按成绩从高到低排序
"""


print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):
    return t[0].lower() # 自建函数

def by_score(t):
    return t[1] # 自建函数

L2 = sorted(L, key=by_name)
print(L2)

L2 = sorted(L, key=by_score)
print(L2)