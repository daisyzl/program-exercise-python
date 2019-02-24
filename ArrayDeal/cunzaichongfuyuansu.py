#-*-coding:utf-8-*-
'''
存在重复元素

题目：https://leetcode-cn.com/problems/contains-duplicate/

答案：https://blog.csdn.net/qq_17550379/article/details/80642667

给定一个整数数组，判断是否存在重复元素。

如果任何值在数组中出现至少两次，函数返回 true。如果数组中每个元素都不相同，则返回 false。

示例 1:

输入: [1,2,3,1]
输出: true
示例 2:

输入: [1,2,3,4]
输出: false
示例 3:

输入: [1,1,1,3,3,4,3,2,4,2]
输出: true

'''


class Solution(object):
    #这样做的弊端是如果是负数，会报错
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums)<1:
            return False
        k = max(nums)
        temp = [0] * (k+1)
        for i in nums:
            temp[i] += 1
        for i in range(len(temp)):
            if temp[i] >=2:
                return True
        return False

    def containsDuplicate2(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 1:
            return False
        if len(nums) != len(set(nums)):
            return True
        return False

    def containsDuplicate2(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 1:
            return False
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False


if __name__ == '__main__':
    li = [99, 22, 64, 55, 11, 35, 89, 1, 1, 2]
    li1 = [-1200000005,-1200000005]
    print(Solution().containsDuplicate(li1))
