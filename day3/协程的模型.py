#coding=utf-8
#Author:gm
def func1(name):
    print('%s准备吃东西了'%(name))
    while True:
        food=yield    #yield卡住跳出函数,send发送数据后继续执行函数
        print('%s被%s吃掉了'%(food,name))
def func2(food):
    f = func1('小明') #创建顾客
    f2= func1('小李')
    f.__next__()       #启动客户,到yield跳出程序
    f2.__next__()
    for i in range(10):
        f.send(food)   #唤醒yield程序并传递food,继续执行print
        f2.send(food)
func2('鱼')
