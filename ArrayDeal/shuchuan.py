#-*-coding:utf-8-*-
'''
题目描述
设有n个正整数，将他们连接成一排，组成一个最大的多位整数。
如:n=3时，3个整数13,312,343,连成的最大整数为34331213。
如:n=4时,4个整数7,13,4,246连接成的最大整数为7424613。

输入描述:
有多组测试样例，每组测试样例包含两行，第一行为一个整数N（N<=100），第二行包含N个数(每个数不超过1000，空格分开)。

输出描述:
每组数据输出一个表示最大的整数。

示例1
输入
2
12 123
4
7 13 4 246

输出
12312
7424613

'''
if __name__ == '__main__':

    n=input()
    num=input().split()

    # n =4
    # num = '13 246 7 4'.split()
    s = ''


    def find(array):
        global s
        if len(array) <= 0:
            return

        else:
            a = array[0]
            for b in array:
                if b + a > a + b:
                    a = b
        s += a
        array.remove(a)
        find(array)
        return s


    print(find(num))
#全部都是对字符串进行操作，＋也是字符串的操作
