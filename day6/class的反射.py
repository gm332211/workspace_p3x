class Dog(object):
    def __init__(self,name):
        self.name=name
    def eat(self):
        print('%s 正在吃东西'%self.name)
d=Dog('xiaoming')
choice=input('请输入方法:')
def bulk(self):
    print('%s 在叫喊'%self.name)
#反射对于方法的使用
if hasattr(d,choice): #动态判断是否存在方法
    obj=getattr(d,choice) #动态调用方法
    obj()
    #delattr(d,choice) #动态删除一个方法
else:
    setattr(d,choice,bulk) #动态设置一个反射方法
    obj=getattr(d,choice)
    obj(d) #这里是动态添加的必须要传入self
#反射对于属性的使用
choice2=input('请输入属性:')
if hasattr(d,choice2): #动态判断一个实例变量
    print(getattr(d,choice2)) #动态获取一个实例变量
    #delattr(d,choice2)
else:
    setattr(d,choice2,None) #动态设置一个实例变量(同样也可以修改一个已经存在的实例变量)
    print(choice2,getattr(d,choice2))

