#coding=utf-8
#Author:gm
import shelve,datetime
#底层封装的是pickle
#存放数据
# dic=shelve.open('test_sheve')
# dic['date']=datetime.datetime.now()
# dic.close()
#读取数据
dic=shelve.open('test_sheve')
print(dic.get('date'))#读取单个
dic.items()#读取所有