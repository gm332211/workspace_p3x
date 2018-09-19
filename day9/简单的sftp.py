import paramiko
#创建sftp连接主机
transport=paramiko.Transport(('192.168.1.10',22))
#连接主机
transport.connect(username='root',password='000000')
#创建sftp类
sftp=paramiko.SFTPClient.from_transport(transport)
#下载文件到本地
sftp.get('/root/anaconda-ks.cfg','test-sftp')
#上传文件到远程
sftp.put('test-sftp','/root/test-sftp')