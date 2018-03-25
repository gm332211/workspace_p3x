#coding=utf-8
#Author:gm
import configparser
#写入文件
# conf=configparser.ConfigParser()
# conf['DEFAULT']={
#     'connection':'http://192.168.100.10:5000/v3'
# }
# conf['auth']={
#     'name': 'admin',
#     'password': '000000'
# }
# f=open('test.ini',encoding='utf-8',mode='w')
# conf.write(f)
# f.close()
#读取文件
conf=configparser.ConfigParser()
conf.read('test.ini')
default=conf.defaults()
auth=conf['auth']
for key in default:
    print(key,default[key])
for key in auth:
    print(key,auth[key])
#删除一个
conf.remove_section('test')
f=open('test.ini','w')
conf.write(f)
#判断
print(conf.has_section('auth'))


