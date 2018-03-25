#coding=utf-8
#Author:gm

#字典的创建
# fruit={}
# fruit={'one':'apple','two':'banana','three':'cherry'}
# fruit=dict.fromkeys(['1','2',3],{'name':'gm'})#创建一个字典,但是这个字典同列表的copy有点相似
#字典的查询
# print(fruit['one'])#获取值,但没有'one'的时候会报错
# print(fruit.get('one'))#获取值
# print(fruit.keys())#获取所有的键
# print(fruit.values())#获取所有的值
#字典的删除
# del fruit['one']#指定删除,但没有one会报错
# fruit.pop('one')#指定删除,同样没有'one'会报错
# fruit.popitem()#随机删除
# fruit.clear() #清空字典
#字典的修改
# fruit['four']='pear'#如果'four'存在这修改,不存在就创建
# fruit.update({'one':'apple juice','five':'petter'})#如果有就修改,没有就添加
# fruit.setdefault('one','apple core')#如果'one'存在不修改,不存在创建
#字典其他函数
# fruit.items()#转换成列表
# fruit.copy()#同列表的copy一样
#字典的循环
# for i in fruit:
#     print('key:%s value:%s'%(i,fruit[i]))
# for k,val in fruit.items(): #不建议使用效率低
#     print(k,val)