#coding=utf-8
#Author:gm
import time
#中国的世界时区UTC+8(东八区+8hours)
#获取时间
print(time.time())#时间戳从1970~现在所有的秒数
print(time.sleep(1))#等待时间
#默认值 时间戳
print(time.localtime())#获取当前时间以元组的表示
print(time.gmtime())#获取世界时间以元组的表示
print(time.ctime())#转化指定的格式化时间(%a %b %d %H:%M:%S %Y)
#默认值 时间元组
print(time.strftime('%Y-%m-%d %H:%M:%S'))#格式化时间元组
tm=time.strftime('%Y-%m-%d %H:%M:%S')
print(time.strptime(tm,'%Y-%m-%d %H:%M:%S'))#格式化时间转时间元组
print(time.asctime())##转化指定的格式化时间(%a %b %d %H:%M:%S %Y)

import datetime
print(datetime.datetime.now())#获取当前格式化后的时间
#默认值 天(year,hours,minutes,seconds......)
print(datetime.datetime.now()+datetime.timedelta(3))#三天后的时间
print(datetime.datetime.now()+datetime.timedelta(-3))#三天前的时间
print(datetime.datetime.now()+datetime.timedelta(hours=2))#二小时后的时间
#默认时间 年
print(datetime.datetime.now().replace(3))#替换当前时间
