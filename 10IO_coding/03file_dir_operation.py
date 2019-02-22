#!/usr/bin/env python
# encoding: utf-8
"""
@Author     :xinbei
@Software   :Pycharm
@File       :03file_dir_operation.py
@Time       :2019/2/21 14:15
@Version    :
@Purpose    :
"""
import os
import platform

# print(os.name) # nt： windows
# print(platform.uname())
# os.path.abspath('.')
# os.path.join(r'first', r'second')
# os.mkdir(r'path_name')
# os.rmdir(r'path_name')
# os.path.splitext(r'first/second')
# os.rename(r'original', r'now')
# os.remove(r'path_name')
# os.listdir(r'path_name') # 当前目录为'.'
# os.path.getmtime(r''))
# os.path.getsize(r'')
# os.path.isdir(r'dir_name')
# os.path.isfile(r'file_path')

"""
1.利用os模块编写一个能实现dir -l输出的程序。
"""
from datetime import datetime
import os
def self_dir():
    pwd = os.path.abspath('.')
    print('      Size     Last Modified  Name')
    print('------------------------------------------------------------')
    for f in os.listdir(pwd):
        fsize = os.path.getsize(f)
        mtime = datetime.fromtimestamp(os.path.getmtime(f)).strftime('%Y-%m-%d %H:%M')
        flag = '/' if os.path.isdir(f) else ''
        print('%10d  %s  %s%s' % (fsize, mtime, f, flag))

# self_dir()
"""
2.编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径。
"""
pwd = os.path.abspath('.')
s = 'test'
def find_test(path_mes, mes):
    for fn in os.listdir(path_mes) :
        fpn = os.path.join(os.path.abspath(path_mes), fn)
        if os.path.isfile(fpn) and mes in fn:
            print(fpn, '\t', ' is a standardized file')
        if os.path.isdir(fn):
            # print(fn, ' is a directory')
            find_test(os.path.abspath(fn), mes)

find_test(pwd, s)
if __name__ == '__main__':
    pass