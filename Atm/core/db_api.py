#coding=utf-8
#Author:gm
import os,sys
BASE_PATH=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_PATH)

def file_handling(path,username):
    '''文件获取用户信息'''
    from core import file_api
    file_path='%s/account/%s.json'%(path,username)
    return file_api.file_read(file_path)
def local_handling(path):
    pass

def getting_data(username):
    '''获取用户的信息'''
    from conf import setting
    engine=setting.DB_SETTING['engine']
    path=setting.DB_SETTING['path']
    if engine=='file':
        user_data=file_handling(path,username)
        return user_data
    elif engine=='localhost':
        local_handling(path)
