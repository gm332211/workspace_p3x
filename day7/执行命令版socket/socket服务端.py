import socket
import os
server=socket.socket()
server.bind(('localhost',8019))
server.listen(5)
print('等待客户端连接')
while True:
    conn,addr=server.accept() #等待客户端的连接
    print('客户端%s:%s 连接成功'%(addr[0],addr[1]))
    while True:
        try:
            cmd=conn.recv(1024) #接收客户端命令
        except Exception as e:
            print('客户端断开连接');break
        if not cmd:print('客户端断开连接');break
        print('执行命令:%s'%cmd.decode('utf-8'))
        data=os.popen(cmd.decode('utf-8')).read() or '没有这个命令' #执行客户端的命令
        data_size= len(data.encode('utf-8'))
        print('发送数据大小:%s' %data_size)
        conn.send(str(data_size).encode('utf-8'))#发送数据的长度
        conn.recv(1024) #防止粘包操作
        conn.send(data.encode('utf-8')) #发送执行命令
server.close()