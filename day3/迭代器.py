#coding=utf-8
#Author:gm
#可迭代对象:可以用for循环的对象都是可迭代对象,如列表元组字典字符串
#迭代器:内部有__next__()方法的对象都是迭代器,如生成器,但迭代器不是生成器
#python3中range(10),文件都是迭代器
#可迭代对象变成迭代器:iter([1,2,3])
print(iter([1,2,3]).__next__())
from collections import Iterable
from collections import Iterator
print(isinstance([1,2,3,4],Iterable))#判断是不是可迭代对象
print(isinstance(iter([1,2,3,4]),Iterator))#判断是不是迭代器
for i in iter([1,2,3,4]):
    print(i)