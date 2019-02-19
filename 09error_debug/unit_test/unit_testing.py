#!/usr/bin/env python
# encoding: utf-8
"""
@Author     :xinbei
@Software   :Pycharm
@File       :unit_testing.py
@Time       :2019/2/19 16:43
@Version    :
@Purpose    :
"""
import unittest
from mydict_test import *
""""    
测试用例放到一个测试模块里，就是一个完整的单元测试
"""
class Dict(dict):

    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value


if __name__ == '__main__':
    d = Dict(a=1, b=2)
    print(d['a'])
    print(d.a)
    pass