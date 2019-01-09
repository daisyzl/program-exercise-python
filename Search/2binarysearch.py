#-*-coding:utf-8-*-
'''
二分查找

前提：线性表是要经过排序

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

     left,right=0,len(nums)
     while left<right:
        mid = (left+right)//2
        if nums[mid] ==target:
            return mid
        elif nums[mid]<target:
             left=mid+1
        else:
              right=mid

     if left !=len(nums) and nums[left]==target:
         return left
     return -1
if __name__=='__main__':
    nums=[1, 5, 7, 8, 22, 54, 99, 123, 200, 222, 444]
    print(binarySearch(nums, 123))



