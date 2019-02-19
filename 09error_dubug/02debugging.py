#!/usr/bin/env python
# encoding: utf-8
"""
@Author     :xinbei
@Software   :Pycharm
@File       :02debugging.py
@Time       :2019/2/19 13:02
@Version    :
@Purpose    :
"""
import logging # 2
import pdb # 4

logging.basicConfig(level=logging.INFO) # 配置logging level，该等级及以上才会输出
# logging.basicConfig(level=logging.DEBUG,#控制台打印的日志级别
#                     filename='02log.log',
#                     filemode='a',##模式，有w和a，w就是写模式，每次都会重新写日志，覆盖之前的日志
#                     #a是追加模式，默认如果不写的话，就是追加模式
#                     format=
#                     '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
#                     #日志格式
#                     ) #  保存log到文件

"""
1.断言,以后启动解释器可以用python -O NAME.py来关闭assert
"""
# def foo1(s):
#     n = int(s)
#     assert n != 0, 'n is zero!'
#     return 10 / n
#
# def main1():
#     foo1('0')


"""
2. logging不会抛出错误，而且可以输出到文件
"""
# s = '0'
# n = int(s)
# logging.info('n = %d' % n) # logging输出信息
# print(10 / n)


"""
3.pdb,让程序以单步方式运行，可以随时查看运行状态.方式： python -m pdb NAME.py
l： 查看代码
n： 单步执行代码
p 变量名： 查看变量
q： 结束调试
"""


"""
4.pdb模块，在可能出错的地方放一个pdb.set_trace(),命令行运行时就会自动进入pdb调试环境
"""


"""
5. IDE设置断点、单步执行
"""
s = '0'
n = int(s)
print(10 / n)


if __name__ == '__main__':
    # main1()

    pass