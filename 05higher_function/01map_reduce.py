#!/usr/bin/env python
# encoding: utf-8
"""
@Author     :xinbei
@Software   :Pycharm
@File       :01map_reduce.py
@Time       :2019/2/14 22:08
@Version    :
@Purpose    :①利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字
             ②请编写一个prod()函数，可以接受一个list并利用reduce()求积：
             ③利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456
"""

from functools import reduce # reduce不同于map，需要导入

def normalize(name): # map
    return name.capitalize()


def prod(L): # map和reduce
    def p(x, y):
        return x*y
    return reduce(p, L)


def str2float(s): # reduce
    return int(s[0:s.index('.')]) + float(s[s.index('.'):])

if __name__ == '__main__':
    # 1.测试map:
    L1 = ['adam', 'LISA', 'barT']
    L2 = list(map(normalize, L1))
    print(L2)

    # 2.测试reduce
    print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
    if prod([3, 5, 7, 9]) == 945:
        print('测试成功2!')
    else:
        print('测试失败2!')

    # 3.测试map和reduce:
    print('str2float(\'123.456\') =', str2float('123.456'))
    if abs(str2float('123.456') - 123.456) < 0.00001:
        print('测试成功3!')
    else:
        print('测试失败3!')
    pass