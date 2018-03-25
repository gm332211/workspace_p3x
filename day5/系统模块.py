#coding=utf-8
#Author:gm
import sys

print(sys.version)#获取python的版本
print(sys.maxsize)#获取机器的int最大值
print(sys.argv)#接收命令行参数,以列表的形式
print(sys.path)#获取python的环境变量
print(sys.platform)#返货操作系统的名称
print(sys.stdout.write('#'))#屏幕输出
val=sys.stdin.readline()[:-1]#标准的输入
sys.exit()#退出程序