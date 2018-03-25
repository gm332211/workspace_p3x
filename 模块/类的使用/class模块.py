class Role():
    #构造函数
    n=123 #类变量，没有实例化也可以调用类变量(好处共用属性，节省内存）
    def __init__(self,name,role,have_gun,live_value=100,money=1000):#类的初始化方法
        self.name=name #实例变量（作用域实例本身）（静态属性）
        self.role=role
        self.have_gun=have_gun
        self.live_value=live_value
        self.money=money
    def buy_gun(self,gun): #类的方法 （动态属性）
        print('%s buy %s'%(self.name,gun))
    def shoot(self):
        print('%s shoot'%(self.name))
    def got_shoot(self):
        print('%s got_shoot'%(self.name))
    def __del__(self):#析构函数，在实例结束后调用
        pass
r1=Role('xiaoming','police','AK74') #实例化类
r1.buy_gun('AWM') #调用类的方法
r1.body_armor='body_armor'#添加实例变量
Role.test='test'#添加类变量
#类变量(好处:共有,节省内存)
#实例变量(静态属性)
#类方法(动态属性)
#构造函数：初始化实例，
#析构函数：做一些收尾工作，关闭数据库连接和临时打开的文件
#私有属性:self.__life_value=100 (只有内部访问）
#私有方法:def __got_shot() (也只有内部可以访问)

# 封装 用户无法访问的内部私有方法 (隐藏实现细节)
# 继承 减少代码重用率(可以扩展已存在的代码模块) 代码重用
# 多态 (一种接口多种实现)                       接口重用