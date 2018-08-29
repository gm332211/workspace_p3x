import threading
class Mythread(threading.Thread):
    def __init__(self,n):
        super(Mythread,self).__init__()
        self.n=n
    def run(self):
        print(self.n)
t1=Mythread('1')
t2=Mythread('2')
t1.start()
t2.start()