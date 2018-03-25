#coding=utf-8
#Author:gm
#列表的创建
#fruit=[] #创建一个空列表
fruit=['apple','banana','cherry']  #创建一个有元素的列表
#列表元素的查找
# print(fruit)#获取全部元素
# print(fruit[:-1])
# print(fruit[:])
# print(fruit[0])#单个元素的获取
# print(fruit[0:3])#print(fruit[:3])顾头不顾尾,获取下标0,1,2
# print(fruit[-1])#获取倒数第一个元素
# print(fruit[-2:-1])#只获取倒数第二个元素
# print(fruit[-2:])#从倒数第二个获取到最后

#列表元素的添加
# fruit.append('pear')#在列表的最后添加元素
# fruit.insert(1,'grape')#在下标1的位置添加元素,其他元素后移一位
# fruit[0]='tomato' #元素的替换

#列表元素的删除
# fruit.remove('tomato')#使用名称移除一个元素
# del fruit[0]#使用下标移除元素
# fruit.pop(index=0)#效果同上,默认移除最后一个
# fruit.clear() #清空列表所有的元素
# del fruit#删除列表


#列表其他函数
# print(fruit.index('apple'))#下标的查找
# print(fruit.count('apple'))#元素个数的统计
# fruit.sort()#按照ASCII码排序
# fruit.reverse() #反转列表
# fruit.extend([1,2,3])#添加列表到fruit列表尾部
# fruit2=fruit.copy() #第一层独立复制,第二层复制的是内存地址
# fruit2=fruit[:]       #同上
# fruit2=list(fruit)    #同上
# import copy
# fruit2=copy.deepcopy(fruit)#真正的完全复制
#列表循环
for i in fruit:
    print(i)
for i in range(len(fruit)):
    print(fruit[i])
for index,data in enumerate(fruit):
    print(index,data)





