#coding=utf-8
#Author:gm
#创建一个集合
gather_one=set([1,2,3,4,4])
gather_one_son=set([1,2,3])
gather_two=set([3,4,5,6])
# print(gather_one)
#集合之间的关系
print(gather_one.intersection(gather_two))#交集
print(gather_one.symmetric_difference(gather_two))#反向交集
print(gather_one.union(gather_two))#并集
print(gather_one.difference(gather_two))#差集
print(gather_one.issuperset(gather_one_son))#子集
print(gather_one_son.issubset(gather_one))#子集
#集合的添加
gather_one.add(15)#添加一个集合元素
gather_one.update([100,222,333])#添加多个元素
#集合的删除
gather_one.pop()#随机删除一个集合元素
gather_one.discard(15)#删除一个集合元素
gather_one.remove(2)#删除一个指定集合元素
# gather_one.clear()#清空集合
#集合的其他方法
gather_three=gather_one.copy()#和列表的复制效果相同
print(gather_one)