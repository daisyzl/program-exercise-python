#-*-coding:utf-8-*-
'''
插入排序
基本思想：插入排序是一种简单直观的排序算法。它的工作原理是通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，
找到相应位置并插入。插入排序在实现上，在从后向前扫描过程中，需要反复把已排序元素逐步向后挪位，为最新元素提供插入空间。

插入排序的时间复杂度问题
最优时间复杂度：O(n) （升序排列，序列已经处于升序状态）
最坏时间复杂度：O(n2)
稳定性：稳定

https://blog.csdn.net/qq_35164554/article/details/78911102
'''

if __name__ == '__main__':
    def insert_sort(li):
        cnt=len(li)
        for i in range(1,cnt):
            for j in range(i,0,-1):#这里的迭代简单,这里必须是0，因为最后迭代不等于0
                if li[j]<li[j-1]:
                    li[j],li[j-1]=li[j-1],li[j]
                else:
                    break
        return li


    li = [99, 22, 64, 55, 11, 35, 89, 1, 2]
    print(insert_sort(li))
