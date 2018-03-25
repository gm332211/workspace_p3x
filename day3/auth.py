#coding=utf-8
#Author:gm
username='admin'
password='000000'
def auth(auth_type):
    def out(func):
        def wrapper(*args,**kwargs):
            if auth_type=='localhost':
                if local_login():
                    print('登入成功')
                    return func(*args,**kwargs)
                else:
                    print('登入失败')
            elif auth_type=='file':
                if file_login():
                    pass    #文件接口登入
            else:
                print('没有这个登入接口')
        return wrapper
    return out
def file_login():
    print('文件登入正在测试中....')
def local_login():
    user=input('Username:').strip()
    pwd=input('Password:').strip()
    if username==user and password==pwd:
        return True
    return False
def index():
    print('welcome to index page')
@auth(auth_type='localhost')
def home():
    print('welcome to home page')
@auth(auth_type='file')
def bbs():
    print('welcome to bbs page')
index()
home()
bbs()