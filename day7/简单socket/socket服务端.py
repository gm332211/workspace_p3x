import socket
server=socket.socket()
server.bind(('localhost',6999)) #连接本地端口
server.listen(5) #监听端口,5最大的连接数
conn,addr=server.accept() #conn连接成功的实例对象,addr连接的地址和端口
data=conn.recv(1024) #接受客户端数据
print('客户端%s: %s'%(addr,data.decode('utf-8')))
conn.send('你好我是服务器'.encode('utf-8')) #响应客户端