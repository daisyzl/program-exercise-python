#-*-coding:utf-8-*-
import threading

import time


if __name__=='__main__':


    def loop():
        print('thread %s is running' % threading.current_thread().name)
        n = 0
        while n < 5:
            n = n+1
            print('thread %s  >>> %s'%(threading.current_thread().name, n))
            time.sleep(1)
            #延时1秒
        print('thread %s ended', threading.current_thread().name)

    print('thread %s is running...', threading.current_thread().name)
    #返回主线程 MainThread
    t = threading.Thread(target=loop(), name='LoopThread')
    t.start()
    t.join()
    print('thread %s ended ',threading.current_thread().name)
