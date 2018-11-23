#-*-coding:utf-8-*-
'''
希尔排序(相比于堆排序第二难)
基本思想：希尔排序(Shell Sort)是插入排序的一种。也称缩小增量排序，是直接插入排序算法的一种更高效的改进版本。
希尔排序是非稳定排序算法。该方法因DL．Shell于1959年提出而得名。 希尔排序是把记录按下标的一定增量分组，
对每组使用直接插入排序算法排序；随着增量逐渐减少，每组包含的关键词越来越多，当增量减至1时，整个文件恰被分成一组，
算法便终止。

https://blog.csdn.net/qq_35164554/article/details/79142939
'''

if __name__ == "__main__":
    def shell_sort(alist):
        n = len(alist)
        gap = n // 2
        while gap > 0:
            for i in range(gap, n):
                j = i
                while j >= gap:
                    if alist[j] < alist[j - gap]:
                        alist[j], alist[j - gap] = alist[j - gap], alist[j]
                        j -= gap
                        #为了计算被2整除不尽的
                    else:
                        break
            gap //= 2



    list1 = [5, 6, 7, 4, 9, 11, 20, 1,2]
    shell_sort(list1)
    print(list1)
