#coding=utf-8
#Author:gm
import os,time
#处理
os.chdir(r'C:')#改变当前工作路径
print(os.path.join(r'C:',r'\a',r'\b'))#拼接路径
os.system('dir')#在当前系统执行代码
print(os.path.split(r'C:\a\test.text'))#分隔路径和文件名
print(os.path.basename(r'C:\a\test.text'))#获取文件名或最后一个路径
# os.makedirs(r'C:\a\b\c\d')#递归创建多个文件夹
# os.removedirs(r'C:\a\b\c\d')#递归删除空文件夹
# os.mkdir(r'C:\a')#创建一个文件夹
# os.rmdir(r'C:\a')#删除一个空的文件夹
# os.rename('text1','text2')#修改文件名称test1是需要修改的文件
#os.remove(r'C:\a.txt')#删除一个文件

#获取信息
print(os.curdir) #返回当前目录符号('.)
print(os.pardir) #返回当前父级目录符号('..')
print(os.pathsep)#返回当前系统的文件路径符
print(os.sep)#返回当前系统的路径分隔符(windows'\\',linux'\')
print(os.linesep)#返回当前系统的换行符
print(os.name)#返回当前系统的名称
print(os.stat(r'C:'))#获取文件或者目录信息

#获取路径
print(os.getcwd())#获取当前工作路径
print(os.environ)#获取当前系统的path
print(os.path.abspath(__file__))#获取绝对路径
print(os.path.dirname(r'C:\a\test.text'))#获取父级路径
print(os.path.getatime(r'C:'))#文件最后存取时间戳
print(os.path.getmtime(r'C:'))#文件最后修改时间戳
print(time.localtime(os.path.getatime(r'F:\pycrypto-2.6.tar.gz')))

#判断
print(os.path.exists(r'C:\a\test.text'))#当前路径是否存在
print(os.path.isfile(r'C:\a\test.text'))#文件是否存在
print(os.path.isdir(r'C:\a'))#文件夹是否存在
print(os.path.isabs(r'C:\a\test.text'))#是不是绝对路径