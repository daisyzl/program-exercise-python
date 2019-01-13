#-*-coding:utf-8-*-
'''
长度最小的子数组

思想：二分法
时间复杂度：O(n log n）

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
class Solution:
    def _windowEx(self, nums, size, s): #函数是设置窗口的大小，最开始的大小为mid
        sum = 0
        for i in range(len(nums)):
            if i>= size:
                #注意这里要有等于号
                sum -= nums[i-size]
            sum += nums[i]
            if sum >= s:
                return True
        return False

    def minSubArrayLen(self, nums, s):
        left, right = 0, len(nums)-1
        result = 0
        while left<= right:
            mid = (left + right)//2
            if self._windowEx(nums, mid, s):
                right = mid-1
                result = mid
            else:
                left = mid+1
        return result

if __name__ == '__main__':
    nums = [2,3,1,2,4,3]
    s = 7
    print(Solution().minSubArrayLen(nums, s))
