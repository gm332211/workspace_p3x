import socket
client=socket.socket()
client.connect(('localhost',9780))
while True:
    data=input('>>>:').strip()
    if not data:continue
    cmd=data.split()
    try:
        filename=cmd[1]
    except Exception as e:
        print('请输入文件名')
        continue
    client.send(filename.encode())
    data_size=client.recv(1024)
    print(type(data_size.decode()))
    if data_size.decode().isdigit():
        data_size=int(data_size.decode())
        print('文件大小%s' % data_size)
        rec_size=0
        client.send('ready ok'.encode())
        f=open(filename+'.back','wb')
        while rec_size != data_size:
            file_data=client.recv(1024)
            f.write(file_data)
            rec_size+=len(file_data)
        else:
            print('文件传输完毕,传输大小%s'%rec_size)
            f.close()
    else:
        print(data_size.decode())