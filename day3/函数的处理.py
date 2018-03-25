#coding=utf-8
#Author:gm
#3种编程方式
#面向对象对象编程---对象
#过程式编程---过程 #过程没有返回值
def func1():
    print('this is print')
#函数式编程 函数有返回值
#函数的特点,避免写重复代码,保持程序的一致性,可扩展
#创建一个函数
def func2():
    print('haha')
    # 函数的返回值
    # 函数的返回值,没有定义返回None,
    # 有一个返回值返回这个object(可以返回一个函数对象),
    # 有多个则是返回一个元组
    return 0
#直接调用函数
func2()
def func3(x,y,z=5,*args,**kwargs):
    print(x)
    print(y)
    print(z)
#函数的参数
#实际参数(实参):1,2,,3
#形式参数(形参):x,y,z
#默认参数:z=5,(非必须传递)
#位置参数的传递,位置的特性:需要一一对应
func3(1,2,3)
#关键字参数的传递,关键字的特性:不需要一一对应
func3(x=1,y=2,z=3)
#非固定参数
#*args接收多余的位置参数的值,以元组形式
#**kwargs接收多余的关键字参数的值,以字典的方式
#混合参数的传递,特性:位置参数要在关键字参数前面,继承了位置和关键字的特性
func3(1,y=2,z=3)


#局部变量和全局变量
# def test():
#     name='xiaoming'#这是一个局部变量
# global name #定义一个全局变量
#函数的递归(调用本身)
#必须要有明确的结束条件
#每次问题的规模要有所减少
#递归的效率不高
def calc(n):
    print(n)
    if n>0:
        return calc(int(n/2))
calc(10)
#高阶函数(一个函数当参数传递个另一个函数)
def add(a,b,i):
    res=i(a)+i(b)
    print(res)
add(1.222,2.111,int)