#!/usr/bin/env python
# encoding: utf-8
"""
@Author     :xinbei
@Software   :Pycharm
@File       :02filter.py
@Time       :2019/2/15 20:52
@Version    :
@Purpose    :用filter()筛选出回数(从左向右读和从右向左读都是一样的数)
"""

def filter_prime():
    # 构造一个从3开始的奇数序列
    def _odd_iter():
        n = 1
        while True:
            n = n + 2
            yield n

    # 定义一个筛选函数
    def _not_divisible(n):
        return lambda x: x % n > 0

    # 定义一个生成器，不断返回下一个素数
    def primes():
        yield 2
        it = _odd_iter()  # 初始序列
        while True:
            n = next(it)  # 返回序列的第一个数
            yield n
            it = filter(_not_divisible(n), it)  # 构造新序列,可以本身带一个变量再传入另一个变量

    # 打印1000以内的素数:
    for n in primes():
        c = 0
        if n < 1000:
            print(n, end='\t')
            c += 1
        else:
            break

# filter_prime() # 输出1000内的质数

def is_palindrome(n):
    s = str(n)
    for i in range(len(s)):
        if s[i-1]!=s[-i]:
            return False
    return True


# 测试:
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == \
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101,
         111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')