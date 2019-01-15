#-*-coding:utf-8-*-
import threading

class Singleton(object):

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if not hasattr(Singleton, "_instance"):
            Singleton._instance = object.__new__(cls)
        return Singleton._instance



def task(arg):
    obj = Singleton()
    print(obj)

if __name__ == '__main__':

    for i in range(10):
        t = threading.Thread(target=task,args=[i,])
        t.start()