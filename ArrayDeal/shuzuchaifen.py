#-*-coding:utf-8-*-
'''
数组拆分 I

思想：要先排序，这样小的元素和除了它外最小的组合才不会牺牲大的。这样和才会最大。
这里用了python list中的sort方法来进行排序。

题目：https://leetcode-cn.com/explore/learn/card/array-and-string/201/two-pointer-technique/784/

给定长度为 2n 的数组, 你的任务是将这些数分成 n 对, 例如 (a1, b1), (a2, b2), ..., (an, bn) ，使得从1 到 n 的 min(ai, bi) 总和最大。

示例 1:

输入: [1,4,3,2]

输出: 4
解释: n 等于 2, 最大总和为 4 = min(1, 2) + min(3, 4).
提示:

n 是正整数,范围在 [1, 10000].
数组中的元素范围在 [-10000, 10000].

'''

class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        listNum = list(nums)
        listNum.sort()
        sum = 0
        for i in range(0, len(listNum), 2):
            sum += listNum[i]
        return sum