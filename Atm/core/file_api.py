#coding=utf-8
#Author:gm
import json
def file_read(path):
    try:
        f=open(path,'r')
    except:
        return 0
    data=json.load(f)
    f.close()
    return data
def file_write(path,data):
    try:
        f=open(path,'w')
    except:
        return 0
    json.dump(data,f)
    f.close()
    return 1
