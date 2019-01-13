#-*-coding:utf-8-*-
'''
长度最小的子数组

思想：滑动窗口
时间复杂度：O(n）

题目：
https://leetcode-cn.com/explore/featured/card/all-about-array/233/sliding-window/971/

答案：
https://blog.csdn.net/qq_17550379/article/details/80540430


给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组。如果不存在符合条件的连续子数组，返回 0。

示例:

输入: s = 7, nums = [2,3,1,2,4,3]
输出: 2
解释: 子数组 [4,3] 是该条件下的长度最小的连续子数组。
进阶:

如果你已经完成了O(n) 时间复杂度的解法, 请尝试 O(n log n) 时间复杂度的解法。

'''


class Solution():
    def minSubArrayLen(self, nums, s):
        left ,right = 0, 0
        n = len(nums)
        min_lenghth = n+1
        sum_all = 0
        while left < n:
            if right < n and sum_all < s:
                sum_all += nums[right]
                right +=1
            else:
                sum_all -= nums[left]
                left +=1
            if sum_all >= s:
                min_lenghth = min(min_lenghth, right - left)
        if min_lenghth == n+1:
            return 0
        return min_lenghth

if __name__ == '__main__':
    nums = [2,3,1,2,4,3]
    s = 7
    print(Solution().minSubArrayLen(nums, s))