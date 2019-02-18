#!/usr/bin/env python
# encoding: utf-8
"""
@Author     :xinbei
@Software   :Pycharm
@File       :06decorator.py
@Time       :2019/2/18 12:58
@Version    :
@Purpose    :
"""


def func1():
    pass


if __name__ == '__main__':
    while True:
        choice = input('choose: 1.')
        if choice == 1:
            func1()
        elif choice == 0:
            break
    pass