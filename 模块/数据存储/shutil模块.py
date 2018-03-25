#coding=utf-8
#Author:gm
import shutil
# shutil.copy('test.txt','package_test')#指定copy文件的目录
# shutil.copyfileobj(f1,f2)#使用文件句柄copy文件,打开二个文件
# shutil.copyfile('test1','new_file')#使用文件名称copy文件
# shutil.copystat('test1','new_file')#copy文件的状态信息,但不copy内容,必须2个文件存在
# shutil.copymode('test1','test3')#copy文件的权限,但不copy文件的用户和组
# shutil.copytree('package_test','new_test')#递归copy文件目录以及文件
# shutil.rmtree('new_test')#递归删除整个文件目录
# shutil.make_archive('test','zip',root_dir=r'F:\workspace_p3.x\day5',)#压缩(zip,tar,gztar,bztar),需要绝对路径的目录
# shutil.move('test.txt','test2.txt')#移动文件或者重命名
#单独压缩zip格式
import zipfile
#压缩
zf=zipfile.ZipFile('test.zip','w')
zf.write('test2.txt')
zf.close()
#解压
zf=zipfile.ZipFile('test.zip','r')
zf.extractall()#可以设置解压地址
zf.close()
import tarfile
#压缩
tf=tarfile.TarFile('test.tar','w')
tf.add('test2.txt',arcname='test.txt')
tf.close()
#解压
tf=zipfile.ZipFile('test.tar','r')
tf.extractall()#可以设置解压地址
tf.close()