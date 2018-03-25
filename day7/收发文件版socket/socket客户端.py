import socket
client=socket.socket()
client.connect(('localhost',9780))
while True:
    cmd=input('>>:').strip()
    if len(cmd)==0:continue
    client.send(cmd.encode())
    data=client.recv(1024)
    f=open('test.tar.gz','wb')
    f.write(data)
f.close()