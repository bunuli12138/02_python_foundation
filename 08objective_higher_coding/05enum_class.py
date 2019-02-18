#!/usr/bin/env python
# encoding: utf-8
"""
@Author     :xinbei
@Software   :Pycharm
@File       :05enum_class.py
@Time       :2019/2/18 20:51
@Version    :
@Purpose    :
"""
import functools, time
from enum import Enum
from enum import unique

# 计算函数运行时间的装饰器
def run_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        t = time.time()
        result = func(*args, **kw)
        print('%s execute %.6f s' % (func.__name__, time.time() - t))
        return result

    return wrapper


# 2. 定义Enum的子类
@unique
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


@unique
class Gender(Enum):
    Male = 0
    Female = 1

class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

if __name__ == '__main__':
    # 1.定义enum可以 Enum('Enum_name', Iterator member.value)
    M = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
    Animal = Enum('Animal', 'ANT BEE CAT DOG')
    A = Enum('Animal', ['ANT', 'BEE', 'CAT', 'DOG'])
    print(Animal.ANT)
    # for name, member in M.__members__.items():
    #     print(name, '=>', member, ',', member.value)
    print(A.ANT)

    # 2.调用方式一样
    # for name, member in Weekday.__members__.items():
    #     print(name, '=>', member, ',', member.value)

    # 测试:
    bart = Student('Bart', Gender.Male)
    if bart.gender == Gender.Male:
        print('测试通过!')
    else:
        print('测试失败!')