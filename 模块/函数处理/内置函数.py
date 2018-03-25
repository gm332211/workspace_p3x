#coding=utf-8
#Author:gm

#判断
print(bool(1))#布尔值判断
print(all([0,1,1]))#全部为真才为真
print(any([0,1,1]))#有一个为真才为真
print(callable([]))#是不是一个方法,是不是可以调用

#转换
for i in enumerate(['a','b','c']):#获取下标和内容
    print(i)
print(bin(11))#十进制转二进制
print(oct(11))#十进制转八进制
print(hex(15))#十进制转十六进制
bytes('a',encoding='utf-8')#转化成二进制格式
tuple()  # 列表变成元组
frozenset([1,2,3,4])#不可变集合,和元组一样
chr(99)#返回ascii对应的字符
float()#转化浮点
repr(range(10))#把对象转化成字符串
print(type(ascii([1,2,3])))#变成一个字符串的形式,没什么用
a=bytearray('abcd',encoding='utf-8')
a[0]=99#字符串和二进制格式不可以修改,但这个可以修改
print(a)

#计算
print(pow(2,5))#次方
print(abs(-1))#计算绝对值
print(divmod(5,2))#返回商和余数
print(sum([1,2,3,4]))#对一个列表求和
round(1.2222,2)#保留小数点后几位
print(max([1,2,3]))#返回最大值
print(min([1,2,3]))#返回最小值
for i in filter(lambda n:n<5,range(10)):#过滤
    print(i)
for i in map(lambda n:n<5,range(10)):#返回前面的结果
    print(i)

#查看
#help()#帮助
print()#打印
print('{name}'.format(name='22'))#格式化输出
type('a')#查看数据类型
print(dir({}))#查看内置方法
vars()#返回一个对象所有的属性名
globals()#打印全局变量的key和value
def func1():
    a=1
    print(locals())#打印全部的局部变量
func1()










#列表和迭代器操作
reversed([1,2,3])#翻转
print(sorted([2,1,3,4]))#排序
print(sorted({2:22,1:33,}.items()))#key排序
print(sorted({2:22,1:33,}.items(),key=lambda x:x[1]))#value排序
zip([1,2,3,4],['a','b','c','d'])#拉链
range(10)#从0取到10不包括10的一个迭代器
#next()#迭代器使用的next方法
list=[1,2,3,4,5,6,7,8,9,10]
print(list[slice(2,5)])#对一个类表切片 没啥用

#其他
#eval()#执行简单的代码块
#exec()#执行多段代码块
__import__('auth')#字符串导入一个模块
#exit()#退出
#hash()#加密
code='''for i in range(10)'''
#compile()#编译 没啥用
complex()#复数用不到
import functools
print(functools.reduce(lambda a,b:a+b,range(10)))#求和
#super
#memoryview
#property
#credits()
#copyright()
#delattr()