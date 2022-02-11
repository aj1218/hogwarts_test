import _thread
import logging
import threading
from time import sleep, ctime

logging.basicConfig(level=logging.INFO)

# def loop0():
#     logging.info("sleep liop0 at"+ctime())
#     sleep(4)
#     logging.info("end liop0 at" + ctime())
#
# def loop1():
#     logging.info("sleep liop1 at" + ctime())
#     sleep(2)
#     logging.info("end liop1 at" + ctime())
#
# def main():
#     logging.info("start all at" + ctime())
#     _thread.start_new_thread(loop0,())
#     _thread.start_new_thread(loop1,())
#     sleep(5)    #_thead  没有守护线程的概念 如果不使用sleep等待,主线程直接退出
#     logging.info("end all at" + ctime())
#
# if __name__ == '__main__':
#     main()

# 设置线程的时间
loops=[2,4]
# nloop :代表现在处于第几个loop
# nsec  ：时间
# lock  ：锁 首先传一个已经锁上的锁
# 当所有的锁都执行完毕 所有的锁都会解开
class MyThread(threading.Thread):
    def __init__(self,func,args,name=""):
        threading.Thread.__init__(self)
        self.func=func
        self.args=args
        self.name=name
    def run(self):
        self.func(*self.args)

def loop(nloop,nsec):
    logging.info("start loop " + str(nloop)+ " at "+ctime())
    sleep(nsec)
    logging.info("end loop "+ str(nloop)+ " at "+ctime())

def main():
    logging.info("start all at "+ ctime())
    #设置锁v
    threads=[]
    nloops = range(len(loops))
    for i in nloops:
        #声明一个锁
        t = MyThread(loop,(i,loops[i]),loop.__name__)
        #把所有的锁都给locks
        threads.append(t)
        # 起线程
    for i in nloops:
        threads[i].start()
    for i in nloops:
        threads[i].join()
    logging.info("end all at" + ctime())


# def main():
#     logging.info("start all at "+ ctime())
#     #设置锁v
#     locks=[]
#     nloops = range(len(loops))
#     for i in nloops:
#         #声明一个锁
#         lock = _thread.allocate_lock()
#         #把锁锁上  加锁
#         lock.acquire()
#         #把所有的锁都给locks
#         locks.append(lock)
#         # 起线程
#     for i in nloops:
#         # 启动子线程
#         _thread.start_new_thread(loop, (i,loops[i],locks[i]))
#     for i in nloops:
#         while locks[i].locked(): pass
#     logging.info("end all at" + ctime())
# def main():
#     logging.info("start all at "+ ctime())
#     #设置锁v
#     threads=[]
#     nloops = range(len(loops))
#     for i in nloops:
#         #声明一个锁
#         t = threading.Thread(target=loop,args=(i,loops[i]))
#         #把所有的锁都给locks
#         threads.append(t)
#         # 起线程
#     for i in nloops:
#         threads[i].start()
#     for i in nloops:
#         threads[i].join()
#     logging.info("end all at" + ctime())


if __name__ == '__main__':
    main()