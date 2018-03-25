#coding=utf-8
#Author:gm
#知识点运用
#函数只有定义和执行
#函数即变量
def func1():
    print('this is func1')
a=func1 #func1这里是一内存地址,a指向内存地址,函数即变量
a()
#高阶函数
#1.把一个函数地址当做实际参数传递个另一个函数
def func2():
    print('this is func2')
def func3(func2):
    func2()
    print('this is func3')
func3(func2)
#2.return返回一个函数的地址
def func4():
    print('this is func4')
    return func5
def func5():
    print('this is func5')
func5=func4()
func5()
#函数的嵌套
def func6():
    print('this is func6')
    def func7():
        print('this is func7')
    func7()
func6()
