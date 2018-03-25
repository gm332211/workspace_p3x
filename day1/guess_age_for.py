#coding=utf-8
#Author:gm
age_of_my=22
for i in range(0,3): #判断的条件
    age=input('age:')
    age=int(age)
    if age_of_my==age:  #判断语句
        print('guess ok')
        break   #跳出循环的语句
    elif age>age_of_my:
        print('think smaller..')
    else:
        print('think bigger...')   #计数器自增
else:   #while条件不成立执行
    print('you tried to many time...')
