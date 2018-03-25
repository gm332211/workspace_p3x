class dog(object):
    '''这是创建狗的类'''
    def __init__(self,name): #构造方法
        self.name=name
    def eat(self):
        print('%s 正在吃狗粮'%self.name)
    def __del__(self): #析构方法
        print('实例释放完毕')
    def __call__(self, *args, **kwargs): #对象在加()调用
        print('我是call方法')
    def __str__(self):
        return 'object<%s>'%self.name #diy自定义返回对象的名称
d=dog('xiaoming')
print(dog.__doc__)#打印类的描述信息
print(d.__module__)#打印当前对象的类导入目录
print(d.__class__)#打印当前对象的类名称
print(dog.__dict__)#查看类下面的所有成员
print(d.__dict__) #查看实例下面的属性
print(d) #str方法的调用
d() #这是call方法的调用

class Foo(object):#可以封装自定义字典
    def __init__(self):
        self.data={}
    def __getitem__(self, item): #获取
        print(self.data.get(item))
    def __setitem__(self, key, value): #设置
        print(key,value)
        self.data[key]=value
    def __delitem__(self, key): #删除
        del self.data[key]
        print('已删除%s'%key)
dic=Foo()
dic['name']='xiaoming'
print(dic['name'])
del dic['name']
print(dic['name'])