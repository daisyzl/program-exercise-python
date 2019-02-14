#-*-coding:utf-8-*-
'''
最大连续1的个数

题目：https://leetcode-cn.com/explore/learn/card/array-and-string/201/two-pointer-technique/788/

给定一个二进制数组， 计算其中最大连续1的个数。

示例 1:

输入: [1,1,0,1,1,1]
输出: 3
解释: 开头的两位和最后的三位都是连续1，所以最大连续1的个数是 3.
注意：

输入的数组只包含 0 和1。
输入数组的长度是正整数，且不超过 10,000。


'''

class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_length = 0
        cnt = 0
        for i in nums:
            if i == 1:
                cnt  += 1
            else:
                cnt = 0
            max_length = max(max_length, cnt)
        return max_length

if __name__ == '__main__':
    nums = [1,0,1,1,0,1]
    print(Solution().findMaxConsecutiveOnes(nums))