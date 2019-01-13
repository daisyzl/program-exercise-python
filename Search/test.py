#-*-coding:utf-8-*-

class Solution():
    def binarySearch(self,nums,target):
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
    nums=[1, 5, 7, 8, 22, 54, 99, 123, 200, 222, 444]
    print(Solution().binarySearch(nums, 222))

