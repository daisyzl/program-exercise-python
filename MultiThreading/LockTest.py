#-*-coding:utf-8-*-
import threading

if __name__ == '__main__':
    balance = 0

    #先定义锁
    lock = threading.Lock()

    def change_it(n):
        global balance
        balance = balance + n
        balance = balance - n

    def run_thread(n):
        for i in range(100000):
            #先获取锁
            lock.acquire()
            try:
                change_it(n)
            finally:
                lock.release()
            #用try...finally来确保锁一定会被释放
