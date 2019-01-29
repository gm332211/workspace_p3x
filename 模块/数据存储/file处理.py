#coding=utf-8
#Author:gm
#文件的打开
# f=open('file_test.text','r',encoding='utf8')#只读打开文件
# f=open('file_test.text','w',encoding='utf8')#写的方式打开文件(有这个文件就会覆盖)
# f=open('file_test.text','a',encoding='utf8')#追加的方式打开文件(append)
f=open('file_test.text','r+',encoding='utf8')#读写方式,先读后写,写入以追加的模式
# f=open('file_test.text','w+',encoding='utf8')#写读,先写后读,写入以覆盖的方式
# f=open('file_test.text','a+',encoding='utf8')#追加读,
# f=open('file_test.text','rb',encoding='utf8')#以二进制的形式读取文件
# f=open('file_test.text','wb',encoding='utf8')#以二进制的形式写入文件
# f=open('file_test.text','ab',encoding='utf8')#以二进制的形式追加文件
# f=open('file_test.text','rU',encoding='utf8')#适配windows和linux的换行
# f=open('file_test.text','r+U',encoding='utf8')#适配windows和linux的换行
#文件写入
f.write('床前明月光,\n疑是地上霜,\n举头望明月,\n低头思故乡.')#写入
f.writelines(['1','2','3'])#以类表的形式写入数据
#文件读取
print(f.readline())#读取一行
print(f.read())#读取所有文件
print(f.readlines())#读取所有变成列表的形式
#文件关闭
f.close()#关闭
f=open('file_test.text','r',encoding='utf8')#打开
#光标移动
# f.seek(0)#光标移动
# f.tell()#当前光标所在的位置
#判断
print(f.readable())#是否可读
print(f.writable())#是否可写入
print(f.seekable())#是否可移动光标
print(f.closed)#是否可关闭
f.isatty()#是不是一个终端设备
#其他文件的函数
# f.flush()#刷新内存中的文件保存
# f.truncate(10)#截断10个字符,10以后的字符会去掉
# f.fileno()#返回文件句柄的编号
# f.detach()#文件编辑过程中改变编码
# print(f.encoding)#文件的编码
# print(f.errors)#文件的报错
#循环
# for line in f:          #最效率
#     print(line.strip())
# for line in f.readlines():
#     print(line.strip())


