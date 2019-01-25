#-*-coding:utf-8-*-

import threading
import time

if __name__ == '__main__':

    # 商品
    product = None
    # 条件变量
    con = threading.Condition()


    # 生产者方法
    def produce():
        global product

        if con.acquire():
            while True:
                print('product  produce222', product)
                if product is None:
                    print ('produce...')
                    product = 'anything'

                    # 通知消费者，商品已经生产
                    con.notify()
                    print('produce...111')

                # 等待通知
                con.wait()
                print('produce...333')
                time.sleep(2)


    # 消费者方法
    def consume():
        global product

        if con.acquire():
            while True:
                print('product  consume222',product)
                if product is not None:
                    print ('consume...')
                    product = None

                    # 通知生产者，商品已经没了
                    con.notify()
                # notify(): 调用这个方法将从等待池挑选一个线程并通知，收到通知的线程将自动调用acquire()尝试获得锁定（进入锁定池）；
                # 其他线程仍然在等待池中。调用这个方法不会释放锁定。使用前线程必须已获得锁定，否则将抛出异常
                print('consume...111')
                # 等待通知
                con.wait()
                #wait([timeout]): 调用这个方法将使线程进入Condition的等待池等待通知，并释放锁。使用前线程必须已获得锁定，否则将抛出异常
                print('consume...333')
                time.sleep(2)


    t1 = threading.Thread(target=produce)
    t2 = threading.Thread(target=consume)
    t2.start()
    t1.start()

