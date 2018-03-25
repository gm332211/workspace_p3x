#coding=utf-8
#Author:gm
def login(username,pwd):
    '''主要用户登入逻辑判断'''
    from core import db_api
    #获取用户数据
    user_data=db_api.getting_data(username)
    #主逻辑判断
    if user_data:
        if user_data['username']==username and user_data['password']==pwd:
            print('登入成功')
            return user_data
        else:
            print('用户名或密码不正确')
    else:
        print('没有这个用户')


