#-*-coding:utf-8-*-
'''
寻找旋转排序数组中的最小值
题目：https://leetcode-cn.com/explore/learn/card/binary-search/210/template-ii/842/




'''
class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, len(nums)
        while l < r:
            mid =(l+r)//2
            if nums[mid]<nums[mid+1]:
                r = mid+1
            else:
                l = mid
        return l
if __name__ == "__main__":
    nums = [3,4,5,1,2]
    print(Solution().findMin(nums))