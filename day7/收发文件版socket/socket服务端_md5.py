import socket,os,hashlib
'''
1.等待连接
2.接收文件名
3.发送文件大小
4.打开指定文件
5.等待请求确认
6.发送文件
7.关闭文件
'''
server=socket.socket()
server.bind(('localhost',9780))
server.listen(5)
while True:
    conn,addr=server.accept()
    print('客户端%s:%s 连接成功' % (addr[0], addr[1]))

    while True:
        try:
            data=conn.recv(1024)
        except Exception as e:
            print('客户端断开连接');break
        filename=data.decode() #接收命令和文件参数
        if os.path.isfile(filename):
            file_size=os.stat(filename).st_size
            conn.send(str(file_size).encode())
            conn.recv(1024)
            f=open(filename,'rb')
            m = hashlib.md5()
            for line in f:
                conn.send(line)
                m.update(line)
            f.close()
            conn.send(m.hexdigest().encode())
        else:
            conn.send('没有文件'.encode())
        print('传输完毕')


