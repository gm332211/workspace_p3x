import socket
import os
server=socket.socket()
server.bind(('localhost',8019))
server.listen(5)
print('等待客户端连接')
conn,addr=server.accept()
print('客户端%s:%s 连接成功'%(addr[0],addr[1]))
while True:
    cmd=conn.recv(1024)
    data=os.popen(cmd.decode('utf-8')).read()
    print(data)
    conn.send(data.encode('gbk'))
server.close()