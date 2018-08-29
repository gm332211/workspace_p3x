import threading
import time
def run(n):
    print(n)
    time.sleep(10)
# run(1)
# run(2)
t1=threading.Thread(target=run,args='2')
t3=threading.Thread(target=run,args='3')
t1.start()
t3.start()