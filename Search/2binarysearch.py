#-*-coding:utf-8-*-
'''
二分查找

适用于它用于查找需要访问数组中当前索引及其
直接右邻居索引的元素或条件



https://leetcode-cn.com/explore/learn/card/binary-search/210/template-ii/839/

初始条件：left = 0, right = length
终止：left == right
向左查找：right = mid
向右查找：left = mid+1

时间复杂度O(log(n))

'''
def binarySearch(nums,target):
     if len(nums)==0:
         return -1

     left, right = 0, len(nums)
     cnt = 0
     while left < right:
        mid = (left+right)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
             left  = mid+1
        else:
              right = mid
        cnt +=1
        print("cnt", cnt)
        print("left,right,mid",left, right, mid)
        # print(nums[left], nums[right], nums[mid])

     if left !=len(nums) and nums[left]==target:
         return left
     return -1
if __name__=='__main__':
    nums=[1, 3, 5, 7, 8]
    #数组一定是有序排列的
    print(binarySearch(nums, 7))



