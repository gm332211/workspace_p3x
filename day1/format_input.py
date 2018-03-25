#coding=utf-8
#Author:gm
#注释一行
'''注释多行'''
print('''
1
2
3
''')
name=input('name:')
age=input('age:')
info='我叫%s,今年%s'%(name,age)
info2='我叫{my_name},今年{my_age}'.format(my_name=name,my_age=age)
info3='我叫{0},今年{1}'.format(name,age)
print(info)
print(info2)
#强制类型转换
# int() str() float()