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
    #join所完成的工作就是线程同步，即主线程任务结束之后，进入阻塞状态，一直等待其他的子线程执行结束之后
    print('thread %s ended ',threading.current_thread().name)
