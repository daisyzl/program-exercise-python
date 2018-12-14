#-*-coding:utf-8-*-
import sys

if __name__ == '__main__':
    def consumer():
        print("sdsadasd")
        r = ''
        print("21212121")
        while True:
            n = yield r #r直接返回给调用方produce，n是调用方的参数
            print('0000000')
            print(r)
            print(n)
            if not n:
                return
            print('[CONSUMER] Consuming %s...' % n)
            r = '200 OK'


    def produce(c):
        r=c.send(None)
        print(r)
        n = 0
        while n < 5:
            n = n + 1
            print('[PRODUCER] Producing %s...' % n)
            r = c.send(888)
            print('[PRODUCER] Consumer return: %s' % r)
        c.close()
'''
注意到consumer函数是一个generator，把一个consumer传入produce后：

首先调用c.send(None)启动生成器；

然后，一旦生产了东西，通过c.send(n)切换到consumer执行；

consumer通过yield拿到消息，处理，又通过yield把结果传回；

produce拿到consumer处理的结果，继续生产下一条消息；

produce决定不生产了，通过c.close()关闭consumer，整个过程结束。

整个流程无锁，由一个线程执行，produce和consumer协作完成任务，所以称为“协程”，而非线程的抢占式多任务。
'''

    c = consumer()#首先要生成一个generator对象,然后用next()函数不断获得下一个返回值，不是普通函数
    produce(c)

    # def test():
    #     return "ok1"
    #
    # def test1(str):
    #     print(str+"2")
    #
    #
    # c=test()
    # print(c)
    # test1(c)






