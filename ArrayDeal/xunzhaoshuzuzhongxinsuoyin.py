#-*-coding:utf-8-*-
'''
寻找数组的中心索引

提示：可以不用写，按照暴力方法就可解决问题，对于此类问题，可以了解解题思路即可

思想：可知道如果存在中心索引的话，那么左边的和的二倍，加上中心索引的值，即等于数组和

题目：https://leetcode-cn.com/explore/learn/card/array-and-string/198/introduction-to-array/770/


答案：
https://blog.csdn.net/weixin_42026630/article/details/81146040

给定一个整数类型的数组 nums，请编写一个能够返回数组“中心索引”的方法。

我们是这样定义数组中心索引的：数组中心索引的左侧所有元素相加的和等于右侧所有元素相加的和。

如果数组不存在中心索引，那么我们应该返回 -1。如果数组有多个中心索引，那么我们应该返回最靠近左边的那一个。

示例 1:

输入:
nums = [1, 7, 3, 6, 5, 6]
输出: 3
解释:
索引3 (nums[3] = 6) 的左侧数之和(1 + 7 + 3 = 11)，与右侧数之和(5 + 6 = 11)相等。
同时, 3 也是第一个符合要求的中心索引。
示例 2:

输入:
nums = [1, 2, 3]
输出: -1
解释:
数组中不存在满足此条件的中心索引。
说明:

nums 的长度范围为 [0, 10000]。
任何一个 nums[i] 将会是一个范围在 [-1000, 1000]的整数。



'''

class Solution():
    def pivotIndex(self, nums):
        all = sum(nums)
        temp = 0
        for i in range(1,len(nums)):
            temp += nums[i-1]
            if temp * 2 + nums[i] == all:
                return i
        return -1

    #自己的想法
    def pivotIndex1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        for i in range(n):
            if sum(nums[:i])== sum(nums[i+1:]):
                return i
        return -1



if __name__ == '__main__':
    nums = [1, 7, 3, 6, 5, 6]
    nums1 = [-1,-1,-1,-1,0,1]
    print(Solution().pivotIndex(nums1))