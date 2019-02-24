#-*-coding:utf-8-*-
'''
搜索插入位置

题目：https://leetcode-cn.com/problems/search-insert-position/

答案：

给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

你可以假设数组中无重复元素。

示例 1:

输入: [1,3,5,6], 5
输出: 2
示例 2:

输入: [1,3,5,6], 2
输出: 1
示例 3:

输入: [1,3,5,6], 7
输出: 4
示例 4:

输入: [1,3,5,6], 0
输出: 0

'''

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(len(nums)):
            if target == nums[i]:
                return i
        l , r = 0 , len(nums)-1
        while l<=r:
            mid = (l+r)//2
            print(mid)
            if nums[mid]<target and nums[mid+1]>target:
                print("dddd")
                return mid+1
            elif nums[mid]<target:
                l = mid+1
            else:
                print("wwww")
                r = mid-1
        return len(nums)
if __name__ == '__main__':
    nums = [1,3,5,6]
    target = 2
    print(Solution().searchInsert(nums, target))