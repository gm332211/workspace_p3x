import paramiko
#创建一个ssh类
ssh=paramiko.SSHClient()
#添加主机列表中没有的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
#连接远程主机
ssh.connect(hostname='192.168.1.10',port=22,username='root',password='000000')
#执行命令 stdin输入的命令,stdout返回的结果,stderr错误的结果
stdin,stdout,stderr=ssh.exec_command('a')
result=stdout.read()
error=stderr.read()
ssh.close()
print(result,error)
