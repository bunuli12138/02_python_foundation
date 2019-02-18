#!/usr/bin/env python
# encoding: utf-8
"""
@Author     :xinbei
@Software   :Pycharm
@File       :03multiple_inherit.py
@Time       :2019/2/18 18:13
@Version    :
@Purpose    :不需要复杂而庞大的继承链，只要选择组合不同的类的功能，就可以快速构造出所需的子类
"""
class Animal(object):
    pass

# 大类:
class Mammal(Animal):
    pass

class Bird(Animal):
    pass


# MixIn
class Runnable(object):
    def run(self):
        print('Running...')

class Flyable(object):
    def fly(self):
        print('Flying...')

# 新子类
class Dog(Mammal, Runnable):
    pass

class Bat(Mammal, Flyable):
    pass

if __name__ == '__main__':
    pass