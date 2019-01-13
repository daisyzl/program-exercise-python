#-*-coding:utf-8-*-
'''
二分查找是高级二分查找自己理解写的

'''

class Solution():
    def binarySearch(self,nums,target):
        if len(nums)== 0:
            return -1
        left, right = 0, len(nums)-1
        mid = (left + right)//2
        while mid < right:
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                left = mid
            else:
                right = mid

            mid = (left+right)//2

        if mid == right and nums[mid] == target:
            return mid
        else:
            return -1
if __name__=='__main__':
    nums=[1, 5, 7]
    print(Solution().binarySearch(nums, 5))
