#-*-coding:utf-8-*-

'''
Python and-or以及三目表达式语法

'''
if __name__ == '__main__':

    print(2 and 1)
    #1
    print(2 and 1 and 3)
    # 这种情况下打印的值为3,即整个表达式中最后一个为真的部分
    print(1 and 3 and 0 and 4)
    # 这种情况下打印第一个为假的部分 0
    print(1 and 0 and 3 / 0)
    ##注意这个地方的运算方式与C一样，如果判断这个布尔表达式已经为假，则返回第一个为假的部分，
    # 并且不再进行接下来的计算，这里就不会报告除0的错误

    print(0 or 1 or 1 / 0)
    # 返回的是第一个真值，并且不再继续进行运算，所以没有除0报错
    print(0 or '')
    # 返回的是最后一个假值 #空字符串

    a = "first"
    b = "second"
    print(False and a)
    #False
    print(False or b)
    #second
    print(False and a or b)
    # 输出为second
    print(True and a)
    #first
    print(True and a or b)
    # 输出为first

    #这时候，大家会发现这样使用跟三目表达式很相似，也确实如此，但是有一个问题就是如果a的值为假的时候，
    # 就不能像真的三目表达式一样工作了(这时候会进行and运算之后还会判断 or b的值)，为了解决这个问题，
    # 可以使用列表的方法

    a = "first"
    b = "second"
    print(1 and [a])
    #['first']
    print((1 and [a] or [b])[0])
    #first
    print((0 and [a] or [b])[0])
    #second

    #这部分不太懂
    a = 0
    b = "second"
    print(1 and [a])
    #[0]
    print(0 or [b])
    #['second']
    print((1 and [a] or [b])[0])
    #and运算之后还会判断 or b的值  这样子为0
    print((0 and [a] or [b])[0])
    #就算a的值是假，因为列表元素总是不为空的，所以总是可以得到正确结果

    '''三目运算符'''
    a = "first"
    b = "second"
    result1 = a if 1 > 0 else b
    print(result1)
    #first
    result2 = a if 1 < 0 else b
    print(result2)
    #second
