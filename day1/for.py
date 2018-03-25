#coding=utf-8
#Author:gm
print('---for---')
for i in range(0,10,2): #给i赋值从0~9,2代表的是每次+2重新赋值
    if i==2:            #判断语句
        continue       #跳出本次循环
    elif i==8:          #2次判断
        break          #结束循环
    else:              #所有条件不成立
        print('loop',i)
print('---while---')
count=0
while count<10:
    print('loop', count)
    count+=1