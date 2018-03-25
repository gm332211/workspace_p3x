#coding=utf-8
#Author:gm
a=[i*2 for i in range(10)]#生成表达式
b=(i*2 for i in range(10))#生成器
print(a)
print(b)
#生成器的特点
#优点:不占用内存空间,生成速度快,
#缺点:不能切片,只能保存当前值,前值不能获取
#调用方法
print(b.__next__())#只唤醒
print(b.send(1))#唤醒并发送数据
#函数生成器
def func(x):
    count=0
    while count<x:
        yield count  #保存当前函数的中断状态(断点)
        count += 1
f=func(10)
#当到函数执行到yield跳出函数进行打印,后继续跳到yield位置向下执行
print(f.__next__())
for i in (i*2 for i in range(10)):
    print(i)