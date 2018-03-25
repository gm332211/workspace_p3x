#coding=utf-8
#Author:gm
#装饰器特点:不修改源代码,不修改调用方式
#装饰器实现:高阶函数+函数的嵌套

def logger(funcTest):   #把源代码的内存地址传递给装饰器
    def waps(*args,**kwargs): #封装内部装饰器
        print('befor')        #装饰的内容
        res=funcTest(*args,**kwargs)#调用源代码
        print('after')
        return res            #返回funcTest的结果
    return waps               #返回封装的装饰器
@logger #funcTest=logger(funcTest)
#被装饰函数的源代码
def funcTest(x):
    print('this is test file',x)
    return x
#funcTest=logger(funcTest) #logger返回的是waps的内存地址,
x=funcTest(x=1) #实际调用的是上方的waps,通过内部的waps调用的funcTest
print(x)

