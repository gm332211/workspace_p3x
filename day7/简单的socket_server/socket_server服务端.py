import socketserver
class Mysocketclass(socketserver.BaseRequestHandler): #第一步重构socket_server父类
    def handle(self):                                 #第二步自定义handle客户端交互方法
        print('客户端连接:%s' % self.client_address[0])
        while True:
            try:
                self.data=self.request.recv(1024).strip()
            except ConnectionResetError as e:
                print('客户端断开连接:%s'%self.client_address[0])
                break
            print('指令:%s'%self.data)
            self.request.send(self.data.upper())
if __name__ == '__main__':
    host,port='localhost',9010
    server=socketserver.TCPServer((host,port),Mysocketclass) #第三步创建socket_server实例
    # server=socketserver.ThreadingTCPServer((host,port),Mysocketclass) #多线程
    # server=socketserver.ForkingTCPServer((host,port),Mysocketclass) #多进程
    server.serve_forever()                                   #第四步设置永久形处理连接


