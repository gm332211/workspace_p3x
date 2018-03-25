import socket
server=socket.socket()
server.bind(('localhost',9780))
server.listen(5)
conn,addr=server.accept()
while True:
    cmd=conn.recv(1024)
    f=open('pycrypto-2.6.tar.gz','rb')
    data=f.read()
    conn.send(data)
f.close()

