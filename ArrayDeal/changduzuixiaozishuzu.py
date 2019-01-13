#-*-coding:utf-8-*-

'''
长度最小的子数组

思想：暴力排序
时间复杂度：O(n^2)

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
    '''
    def minSubArrayLen(self, nums, s):
        index_temp = len(nums) + 1
        for i in range(len(nums)):
            temp = 0
            for j in range(i, len(nums)):
                #这种j的序列还是原来nums的序列位置，不是从0开始的
                temp += nums[j]
                if temp >= s:
                    index_temp = min(index_temp, j+1)
        if index_temp == len(nums) + 1:
            return 0
        return  index_temp
    '''


    def minSubArrayLen(self, nums, s):
        n = len(nums)
        index_temp = n + 1
        for i in range(n):
            temp = 0
            for j, val in enumerate(nums[i:]):
                # 这种排序从0开始
                temp += val
                if temp >= s:
                    index_temp = min(index_temp, j + 1)
        if index_temp == n + 1:
            return 0
        return index_temp


if __name__ == '__main__':
    nums = [2,3,1,2,4,3]
    s = 7
    print(Solution().minSubArrayLen(nums, s))

