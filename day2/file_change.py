#coding=utf-8
#Author:gm
f=open('file_test.text','r',encoding='utf8')
f_new=open('file_test.bak','w',encoding='utf8')
for line in f:
    if '举头望明月' in line:
        line=line.replace('举头望明月','举头望太阳')
    f_new.write(line)
    print(line.strip())
f.close()
f_new.close()