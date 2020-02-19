#-*-coding:utf-8-*-
'''
子数组最大平均数 I

题目：https://leetcode-cn.com/problems/maximum-average-subarray-i/

答案：

给定 n 个整数，找出平均数最大且长度为 k 的连续子数组，并输出该最大平均数。

示例 1:

输入: [1,12,-5,-6,50,3], k = 4
输出: 12.75
解释: 最大平均数 (12-5-6+50)/4 = 51/4 = 12.75


注意:

1 <= k <= n <= 30,000。
所给数据范围 [-10,000，10,000]。

'''

#在leetcode没有编译成功
class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        if len(nums)<=1:
            return nums[0]
        if len(nums)==k:
            return sum(nums)/2
        temp =[]
        for i in range(k,len(nums)+1):
            print(nums[i-k])
            print(nums[i-1])
            temp.append(sum(nums[i-k:i]))
            print(sum(nums[i-k:i]))
        return max(temp)/k
if __name__ == '__main__':
    nums = [1,12,-5,-6,50,3]
    k = 4
    print(Solution().findMaxAverage(nums, k))