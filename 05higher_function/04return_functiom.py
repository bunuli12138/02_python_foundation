#!/usr/bin/env python
# encoding: utf-8
"""
@Author     :xinbei
@Software   :Pycharm
@File       :04return_functiom.py
@Time       :2019/2/16 15:51
@Version    :
@Purpose    :利用闭包返回一个计数器函数，每次调用它返回递增整数
"""

# 一定要引用循环变量时：
# 再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变
_list = []
for i in range(3):
    def func(i): # 闭包，传入外部运行环境参数i
        def f_closure(a):  # <<<---
            return i + a

        return f_closure


    _list.append(func(i))  # <<<---

for f in _list:
    print(f(1))





def createCounter():
    def counter():
        def c():
            return i+1
        return c
    for i in range(6):
        return counter

# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')