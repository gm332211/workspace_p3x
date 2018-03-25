class dog(object):
    name='dog'
    def __init__(self,name):
        self.name=name
        self._someting=None
    @staticmethod #静态方法,不能访问内中的任何方法和变量,不能成为实例的方法
    def eat(): #方法内部能传入实例化后的本身(self)
        # print('%s 正在吃饭...'%name)
        print('正在吃饭')
    @classmethod #类方法,不能访问实例方法和实例变量,可以访问类属性和类变量
    def run(self):
        print('%s 正在跑步'%self.name) #只能访问类变量,使用范围(固定用户无法改变的参数)
    @property #方法变成静态属性
    def sleep(self):
        print('%s 正在在%s睡觉' % (self.name, self._someting))
    @sleep.setter #给静态属性赋值,setter
    def sleep(self,someting):
        self._someting=someting
    @sleep.deleter #给静态属性删除赋值
    def sleep(self):
        del self._someting
        print('设置参数被删除了')
d1=dog('xiaoming')
dog.eat()
d1.run()
d1.sleep='bed'
d1.sleep
del d1.sleep
# d1.sleep #传入的参数被删除,这里会报错