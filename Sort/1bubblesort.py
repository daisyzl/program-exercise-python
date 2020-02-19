#-*-coding:utf-8-*-

'''
冒泡排序的原理:每一趟只能将一个数归位, 如果有n个数进行排序, 只需将n - 1个数归位, 也就是说要进行n - 1趟操作(已经归位的数不用再比较)

由小到大，大数先被冒泡出来

'''
from random import randint

if __name__ == '__main__':
    # data=[3, 90, 196, 206, 241, 263, 665, 719, 892, 914]
    data = [randint(1, 999) for i in range(10)]
    # data = [3,4,1]
    def bubbleSort(data):
        for i in range(0,len(data)):
            #i 计算需要多少次循环
            for j in range(0,len(data)-i-1):
                #j 找到每个列表的位置
                if data[j]>data[j+1]:
                    data[j],data[j+1]=data[j+1],data[j]
        return data
    print(bubbleSort(data))
    # def bubbleSort(data):
    #     cnt = 0
    #     for i in range(1,len(data)):
    #         #i 计算需要多少次循环
    #         cnt += 1
    #         if cnt < 3:
    #             for j in range(0,len(data)-i):
    #                 #j 找到每个列表的位置
    #                 if data[j]< data[j+1]:
    #                     data[j],data[j+1]=data[j+1],data[j]
    #         else:
    #             return data[len(data)-2]
    # print(bubbleSort(data))

