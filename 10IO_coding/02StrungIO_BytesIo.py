#!/usr/bin/env python
# encoding: utf-8
"""
@Author     :xinbei
@Software   :Pycharm
@File       :02StrungIO_BytesIo.py
@Time       :2019/2/21 13:54
@Version    :
@Purpose    :
"""
from io import StringIO, BytesIO

"""
创建一个StringIO，然后，像文件一样写入
"""
sio = StringIO()

sio.write('hello')
sio.write(' ')
sio.write('world')

print(sio.getvalue())

"""
读取StringIO，可以用一个str初始化StringIO，然后，像读文件一样读取
"""
sio2 = StringIO('Hello!\nHi!\nGoodbye!')

while True:
    s = sio2.readline()
    if s == '':
        break
    print(s.strip())


# 二进制数据
"""
创建一个BytesIO，然后写入一些bytes
"""
bio = BytesIO()

bio.write('中文'.encode('utf-8'))

print(bio.getvalue())

"""
用一个bytes初始化BytesIO，然后，像读文件一样读取
"""
bio2 = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
bio2.read()
if __name__ == '__main__':
    pass