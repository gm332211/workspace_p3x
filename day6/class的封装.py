class people(object):
    def __init__(self,name):
        self.__name=name #内部封装属性
    def __talk(self):
        print('%s 在说话'%self.__name) #内部属性可以在内部使用
    def help(self):
        self.__talk()#内部方法可以在内部调用
p1=people('xiaoming')
# print(p1.__name)#外部无法访问内部属性和方法
# p1.__talk()
p1.help()