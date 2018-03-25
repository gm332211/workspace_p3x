#coding=utf-8
#Author:gm
age_of_my=22
count=0 #计数器
while count<3: #判断的条件
    age=input('age:')
    age=int(age)
    if age_of_my==age:  #判断语句
        print('guess ok')
        break   #跳出循环的语句
    elif age>age_of_my:
        print('think smaller..')
    else:
        print('think bigger...')
    count=count+1   #计数器自增
    if count==3:
        continue_confirm=input('do you want to keep trying? n(quit)')
        if continue_confirm=='n':
            print('game over')
            break
        else:
            print('The game continue')
            count=0
# else:   #while条件不成立执行
#     print('you tried to many time...')
