#类的起源是type,type的起源是python解释器
#通过type创建一个类
def eat(self):
    print('%s正在吃东西'%self.name)
def __init__(self,name,age):
    self.name=name
    self.age=age
Foo=type('Foo',(object,),{'eat':eat,'__init__':__init__})
f=Foo('xiaoming',22)
f.eat()
class MyClass(type):
    def __init__(self,what,bases=None,dict=None): #继承type的构造方法
        super(MyClass,self).__init__(what,bases,dict)
    def __call__(self, *args, **kwargs): #通过在加()调用 这个就是type的实例(class)
        obj=self.__new__(self,*args,**kwargs) #调用实例化后的type,也就是类的new方法
        self.__init__(obj) #调用类的构造方法
class Foo(object):
    __metaclass__=MyClass
    def __init__(self,name):
        self.name=name
    def __new__(cls, *args, **kwargs): #在构造方法之前执行,调用构造方法
        return object.__new__(cls)
