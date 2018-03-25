#coding=utf-8
#(上面的coding是文件打开的编码
#Author:gm
str='你好'
#encode:编码 Python3中字符默认编码是'unicode'转换成'gbk'或者其他的编码
print(str.encode('gbk'))
#decode解码 'gbk'其他的编码转化成'unicode'编码
print(str.encode('gbk').decode('gbk'))

