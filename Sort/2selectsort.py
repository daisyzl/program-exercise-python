#-*-coding:utf-8-*-
'''

选择排序
基本思想：选择排序是一种简单直观的排序算法。它的工作原理首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，
然后，再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。以此类推，直到所有元素均排序完毕。

选择排序
第一次从下标为0的开始下标为0的这个数与后面的n-1个进行比较；找出最小或者最大的放在下标为0的这个位置；第二次从下标为1的
开始比较；查询剩下的最大或者最小值；放在下标为1的位置；以此类推；直到排序完成



最优时间复杂度：O(n2)
'''
import random

if __name__ == '__main__':
    # def select_sort(li):
    #     cnt=len(li)
    #     for i in range(cnt-1):
    #         min_index=i
    #         for j in range(i+1,cnt):
    #             if li[min_index]>li[j]:
    #                 li[min_index],li[j]=li[j],li[min_index]
    #     return li

    # def select_sort(li):
    #     # cnt=len(li)
    #     for i in range(len(li)-1):
    #         min_index=i
    #         for j in range(i+1,len(li)):
    #             if li[min_index]>li[j]:
    #                 li[min_index],li[j]=li[j],li[min_index]
    #     return li

#方法二
    def select_sort(li):
        for i in range(0, len(li)):
            min_index = i
            for j in range(i, len(li)):
                if li[min_index] > li[j]:
                    min_index = j
            li[min_index], li[i] = li[i], li[min_index]
        return li


    li = [random.randint(1, 999) for i in range(10)]
    print(select_sort(li))


