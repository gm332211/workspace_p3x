#coding=utf-8
#Author:gm
import json,pickle
data={'user':'admin','password':'000000'}
#-------存值--------
f_json=open('json.text','w')
f_pickle=open('pickle.text','wb')
#json可以多平台
json.dump(data,f_json) # ===f_json.write(json.dumps(data))
#pickle只能python使用.必须是二进制
pickle.dump(data,f_pickle)#==f_pickle.write(pickle.dumps(data))
f_json.close()
f_pickle.close()

#-------取值--------
f_json=open('json.text','r')
f_pickle=open('pickle.text','rb')
data_load_json=json.load(f_json)#==data_load_json=json.loads(f_json.read())
data_load_pickle=pickle.load(f_pickle)#==data_load_pickle=pickle.loads(f_pickle.read())
f_json.close()
f_pickle.close()
print(data_load_json)
print(data_load_pickle)