#-*-coding:utf-8-*-

'''
冒泡排序的原理:每一趟只能将一个数归位, 如果有n个数进行排序, 只需将n - 1个数归位, 也就是说要进行n - 1趟操作(已经归位的数不用再比较)
'''

if __name__ == '__main__':
    data=[5,24,45,66,8,3,88,86]
    def bubbleSort(data):
        for i in range(1,len(data)):
            for j in range(0,len(data)-i):
                if data[j]>data[j+1]:
                    data[j],data[j+1]=data[j+1],data[j]
        return data
    print(bubbleSort(data))
