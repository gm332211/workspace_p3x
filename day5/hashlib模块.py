#coding=utf-8
#Author:gm
import hashlib
m=hashlib.md5()
m.update('我是加密文件'.encode(encoding='utf-8'))#必须是二进制格式
print(m.hexdigest())#digest是二进制显示,hexdigest是十六进制显示
m2=hashlib.sha1()
m2.update('我是加密文件二'.encode(encoding='utf-8'))
print(m.hexdigest())
import hmac
#key,value的加密方式
m3=hmac.new('我是文件的key'.encode(encoding='utf-8'),'我是文件的value'.encode(encoding='utf-8'))
print(m3.hexdigest())