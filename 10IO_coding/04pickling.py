#!/usr/bin/env python
# encoding: utf-8
"""
@Author     :xinbei
@Software   :Pycharm
@File       :04pickling.py
@Time       :2019/2/22 12:26
@Version    :
@Purpose    :
"""
import pickle
import json # json is better

"""pickle"""
d = dict(name='Bob', age=20, score=88)

pickle.dumps(d)
print('dump d: ', pickle.dumps(d))

with open(r'04file\dump.txt', 'wb') as fdw:
    pickle.dump(d, fdw)

with open(r'04file\dump.txt', 'rb') as fdr:
    d2 = pickle.load(fdr)
print('load d: ', d2)


"""json"""
d = dict(name='Bob', age=20, score=88)
jd = json.dumps(d)
print('json dump: ', jd, type(jd))
jl = json.loads(jd)
print('json load: ', jl, type(jl))
"""json进阶：类序列化"""
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


def student2dict(std): # 转换为dict
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }
s = Student('Bob', 20, 88)
sd = json.dumps(s, default=student2dict)
print('Student dump: ', sd) # 传入转换方法
print('Student dump: ', json.dumps(s, default=lambda obj: obj.__dict__)) # 除了定义了__slots__的class外的都可以

def dict2student(d):
    return Student(d['name'], d['age'], d['score'])
sl = json.loads(sd, object_hook=dict2student)
print('Student load: ', sl)


"""中文序列化"""
obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=True)
print('s: ', s)
s2 = json.dumps(obj, ensure_ascii=False) # 中文默认ascii编码，需获得中文要将ensure_ascii设为False
print('s2: ', s2)
if __name__ == '__main__':
    pass