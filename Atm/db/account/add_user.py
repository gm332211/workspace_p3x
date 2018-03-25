#coding=utf-8
#Author:gm
import json
data={
    'username':'admin',
    'password':'000000',
    'balance':10000
}
f=open('%s.json'%(data['username']),'w')
json.dump(data,f)
f.close()
