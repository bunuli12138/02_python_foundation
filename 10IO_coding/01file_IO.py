#!/usr/bin/env python
# encoding: utf-8
"""
@Author     :xinbei
@Software   :Pycharm
@File       :01file_IO.py
@Time       :2019/2/21 13:24
@Version    :
@Purpose    :
"""
import os
file_name = '01open.txt'
file2_name = '01write.txt'
try:
    with open(file_name, 'r') as f:
        l = f.readline()
        print(l)

    # 不自动创建文件
    if os.path.exists(file2_name):
        with open(file2_name, 'a') as f2:
            f2.write(l)
    else:
        raise FileNotFoundError
except FileNotFoundError:
    print('%s does not exits!' % file2_name)



if __name__ == '__main__':
    pass