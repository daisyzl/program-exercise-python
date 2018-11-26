#-*-coding:utf-8-*-

'''
快速排序
https://blog.csdn.net/razor87/article/details/71155518

http://note.youdao.com/noteshare?id=a7f3ac029655c3429d01341daece6c8a&sub=WEBf4c2c57e625a3f31982154e0758ecfbe

最优时间复杂度：O(nlogn)
最坏时间复杂度：O(n2)

'''

if __name__ == '__main__':
    def quick_sort(li,low,high):
        if low>=high:
            return
        #注意上面这个条件比较关键，迭代都有一个return 的条件
        left=low
        right=high
        x=li[low]
        while left<right:
            while left<right and li[right]>x:
                right-=1
            li[left]=li[right]
            while left<right and li[left]<x:
                left+=1
            li[right]=li[left]
        li[left]=x
        quick_sort(li,low,left-1)
        quick_sort(li,left+1,high)


    li = [99, 22, 64, 55, 11, 35, 89, 1, 2]
    quick_sort(li,0,len(li)-1)
    print(li)
    #快排是原地排序，因此不需要返回array