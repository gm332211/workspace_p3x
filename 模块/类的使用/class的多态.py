class Dog(object):
    def __init__(self,name):
        self.name=name
    def talk(self):
        print('%s:woof!'%self.name)
class Cat(object):
    def __init__(self,name):
        self.name=name
    def talk(self):
        print('%s:meow!'%self.name)
class Animal(object):
    def talk(self):
        self.talk()
d1=Dog('dabai')
c2=Cat('xiaohua')
Animal.talk(d1)#一种发放多种实现(多态) 给用户统一接口,用户无法知道其中几种接口
Animal.talk(c2)