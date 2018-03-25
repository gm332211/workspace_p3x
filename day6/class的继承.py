class people(object): #共同特性的一个父类
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.friend=[]
    def eat(self):
        print('%s正在吃饭...'%self.name)
    def sleep(self):
        print('%s正在睡觉...'%self.name)
class relation(object): #扩展类,扩展方法的一个父类
    def make_friend(self,obj):
        print('%s 和 %s 成为朋友了...'%(self.name,obj.name))
        self.friend.append(obj)
class man(people,relation): #多继承,从左向右继承
    def __init__(self,name,age,money): #重构方法,重构父类构造函数(覆盖父类重名的方法)
        self.money=money
        super(man,self).__init__(name,age) #重新执行父类初始化方法
    def beard(self):
        print('%s 长胡子了'%self.name)
class woman(people):#类的继承,继承了父类的属性和方法(节省代码,减少代码的重复率)
    def look_book(self):
        print('%s 正在看书...'%self.name)
m1=man('xiaoming',22,100)
m2=man('chengwenliang',22,200)
m1.make_friend(m2)
print('%s 的好友列表:'%m1.name)
for i in m1.friend:
    print(i.name)
# for i in m1.friend:
#     print('%s'%m1.friend[i])
m1.beard()
#多继承构造方法的优先顺序
#py2中默认使用的是经典类:__init__方法采用深度优先(object)采用广度优先
#py3中都采用:广度优先