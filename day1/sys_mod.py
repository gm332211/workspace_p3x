#coding=utf-8
#Author:gm
import sys
for i in sys.path: #sys.path 所有模块的路径
    print(i)
# print(sys.argv)#相对路径
# file_name=sys.argv[0]
# print(file_name)
# import os
# os.makedirs('haha')
# os.system('dir')#执行命令,但不保存结果
# print(os.popen('dir').read())#返回对象,调用read方法获取结果

#数据类型
#int型
#long型
#float型
#布尔型
print(type(2/3))
print(1 in [1,2,3])
print(type(1) is int)
print('哈哈'.encode(encoding='utf8'))
print(b'\xe5\x93\x88\xe5\x93\x88'.decode(encoding='utf8'))
result=1 if 1<2 else 2
print(result)