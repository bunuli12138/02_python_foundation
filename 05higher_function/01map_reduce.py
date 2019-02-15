#!/usr/bin/env python
# encoding: utf-8
"""
@Author     :xinbei
@Software   :Pycharm
@File       :01map_reduce.py
@Time       :2019/2/14 22:08
@Version    :
@Purpose    :①利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字
             ②利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456
"""

from functools import reduce # reduce不同于map，需要导入

def normalize(name):
    return name.capitalize()
    pass



def str2float(s):
    return int(s[0:s.index('.')]) + float(s[s.index('.'):])
    pass


if __name__ == '__main__':
    # 测试map:
    L1 = ['adam', 'LISA', 'barT']
    L2 = list(map(normalize, L1))
    print(L2)

    # 测试reduce
    print('str2float(\'123.456\') =', str2float('123.456'))
    if abs(str2float('123.456') - 123.456) < 0.00001:
        print('测试成功!')
    else:
        print('测试失败!')
    pass