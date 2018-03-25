import socket
client=socket.socket()

client.connect(('localhost',8019))

while True:
    cmd=input('>>:').strip()
    if len(cmd)==0:continue
    client.send(cmd.encode('utf-8'))
    data_size=client.recv(1024)
    client.send('准备就绪'.encode('utf-8'))
    data_size=int(data_size.decode('utf-8')) #接收数据大小
    recv_size=0
    data = ''.encode()
    print('接收数据的大小:%s'%data_size)
    while recv_size != data_size:
        rec=client.recv(1024)
        recv_size+=len(rec)
        data+=rec
    else:
        print(data.decode('utf-8'))
client.close()
