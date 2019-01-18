#-*-coding:utf-8-*-
'''

装饰器  回调函数只能每10s只能被调用一次
'''

def debug(func):
    def wrapper(*args, **kwargs):  # 指定宇宙无敌参数
        print ( "[DEBUG]: enter {}()".format(func.__name__))
        print ('Prepare and say...')
        return func(*args, **kwargs)
    return wrapper  # 返回

@debug
def say(something):
    print ("hello {}!".format(something))