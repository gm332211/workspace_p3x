import socket
#AF_INET ipv4
#SOCK_STREAM tcp/ip
client=socket.socket()
client.connect(('localhost',6999)) #localhost连接的ip地址,连接的端口
client.send('在吗'.encode('utf-8')) #发送数据 在py3上发送的必须是二进制
data=client.recv(1024) #1024接受的字符个数
print(data.decode('utf-8'))