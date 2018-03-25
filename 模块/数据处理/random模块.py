#coding=utf-8
#Author:gm
import random
print(random.random())#0~1随机小数
print(random.uniform(0,2))#0~2之间的随机小数
print(random.randint(0,3))#0~3的随机数
print(random.randrange(0,10))#0~9的随机数(顾头不顾尾)
print(random.choice('abcd'))#随机字符串,或者列表
print(random.sample('abcd',2))#指定随机的个数这里指定'ab'
r=random.shuffle([1,2,3,4,5]) #打乱列表元素
random_str=''
for i in range(4):
    if i==random.randint(0,4):
        tmp=str(random.randint(0,9))
    else:
        tmp=chr(random.randint(67,90))
    random_str+=tmp
print(random_str)#随机验证码
