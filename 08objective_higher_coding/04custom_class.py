#!/usr/bin/env python
# encoding: utf-8
"""
@Author     :xinbei
@Software   :Pycharm
@File       :04custom_class.py
@Time       :2019/2/18 19:30
@Version    :
@Purpose    :
"""
import functools, time


# 计算函数运行时间的装饰器
def run_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        t = time.time()
        result = func(*args, **kw)
        print('%s execute %.6f s' % (func.__name__, time.time() - t))
        return result

    return wrapper


class Fib(object):
    def __init__(self, count, path=''):
        self.count = count # __next__
        self.a, self.b = 0, 1  # 初始化两个计数器a，b
        self._path = path # 链式调用，__getarrt__

    def __str__(self):
        return 'Fib object (count: %s)' % self.count


    def __iter__(self): # for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b  # 计算下一个值
        if self.a > self.count:  # 退出循环的条件
            raise StopIteration()
        return self.a  # 返回下一个值

    def __getitem__(self, n): # 像list一样可以indexing
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a

    def __getattr__(self, path):
        return Fib('%s/%s' % (self._path, path))


class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path): # 因Chain类没有stu方法，python调用该函数，返回当前输入的方法名
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__

    def __call__(self, *args, **kwargs):
        # print('My path is %s.' % self._path)
        return 'My path is %s.' % self._path

if __name__ == '__main__':
    fib = Fib(10)
    print(fib) # __str__
    for f in fib: # __iter__ and __next__
        print(f, end=' ')
    print('\n', fib[11]) # __getitem__

    c = Chain().stu
    print(c.stu.alert.friend) # __getattr__
    print(c()) # __call__,当此方法不返回值时，还有多打印一个None
    
    print(callable(c)) # 可被调用的，c()
    print(callable(fib)) # 不可被调用