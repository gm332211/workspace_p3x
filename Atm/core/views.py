#coding=utf-8
#Author:gm
from core import main
from core import auth
Identity={
    'user_id':None,
    'user_data':None,
    'user_status':False
}
from conf import setting
from core import file_api
def verify(func):
    '''验证用户登入的装饰器'''
    def wrapper(*args,**kwargs):
        if not Identity['user_status']:
            username=input('Username:').strip()
            pwd=input('Password:').strip()
            user_data=auth.login(username,pwd)
            if user_data:
                Identity['user_status']=True
                Identity['user_id']=username
                Identity['user_data']=user_data
                func(*args, **kwargs)
        else:
            func(*args,**kwargs)
    return wrapper

@verify
def user_info():
    '''打印用户信息函数'''
    print('账户名称:%s,余额:$%s'%(
        Identity['user_data']['username'],
        Identity['user_data']['balance']
    ))
@verify
def draw_money():
    '''用户取款逻辑'''
    path = setting.DB_SETTING['path']
    file_path = '%s/account/%s.json' % (path, Identity['user_data']['username'])
    draw=input('需要取款:').strip()
    draw=int(draw)
    data=file_api.file_read(file_path)
    if data['balance']>=draw:
        data['balance']=data['balance']-draw
        file_api.file_write(file_path,data)
        Identity['user_data'] = data
        print('取款$%s,余额:$%s'%(draw,data['balance']))
    else:
        print('余额不足,余额$%s'%(data['balance']))
def save_money():
    '''用户存钱逻辑'''
    path = setting.DB_SETTING['path']
    file_path = '%s/account/%s.json' % (path, Identity['user_data']['username'])
    draw = input('需要存款:').strip()
    draw = int(draw)
    data = file_api.file_read(file_path)
    data['balance'] = data['balance'] + draw
    file_api.file_write(file_path, data)
    Identity['user_data']=data
    print('存款款$%s,余额:$%s' % (draw, data['balance']))