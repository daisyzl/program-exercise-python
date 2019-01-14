#-*-coding:utf-8-*-
'''
单例模式
基于__new__方法实现（推荐使用，方便）

https://www.cnblogs.com/huchong/p/8244279.html

当我们实现单例时，为了保证线程安全需要在内部加入锁

我们知道，当我们实例化一个对象时，是先执行了类的__new__方法（我们没写时，默认调用object.__new__），实例化对象；
然后再执行类的__init__方法，对这个对象进行初始化，所有我们可以基于这个，实现单例模式

__init__和__new__的区别

__new__方法负责创建一个实例对象，在对象被创建的时候调用该方法它是一个类方法。
__new__方法在返回一个实例之后，会自动的调用__init__方法，对实例进行初始化。
如果__new__方法不返回值，或者返回的不是实例，那么它就不会自动的去调用__init__方法。

__init__ 方法负责将该实例对象进行初始化，在对象被创建之后调用该方法，
在__new__方法创建出一个实例后对实例属性进行初始化。__init__方法可以没有返回值。


hasattr(object, name)
判断一个对象里面是否有name属性或者name方法，返回BOOL值，有name特性返回True， 否则返回False。
需要注意的是name要用括号括起来

加锁！未加锁部分并发执行,加锁部分串行执行,速度降低,但是保证了数据安全



'''
import threading
class Singleton(object):
    _instance_lock = threading.Lock()

    #初始化方法
    def __init__(self):
        pass

    #类方法
    def __new__(cls, *args, **kwargs):
        if not hasattr(Singleton, "_instance"):
            #把锁释放了才能进行下部操作
            with Singleton._instance_lock:
                if not hasattr(Singleton, "_instance"):
                    Singleton._instance = object.__new__(cls)
        return Singleton._instance

if __name__ == '__main__':

    obj1 = Singleton()
    obj2 = Singleton()
    print(obj1,obj2)

    def task():
        obj = Singleton()
        print(obj)

    for i in range(10):
        t = threading.Thread(target=task,args=[])
        t.start()