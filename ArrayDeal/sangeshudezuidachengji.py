#-*-coding:utf-8-*-
'''
三个数的最大乘积

题目：https://leetcode-cn.com/problems/maximum-product-of-three-numbers/

给定一个整型数组，在数组中找出由三个数组成的最大乘积，并输出这个乘积。

示例 1:

输入: [1,2,3]
输出: 6
示例 2:

输入: [1,2,3,4]
输出: 24
注意:

给定的整型数组长度范围是[3,104]，数组中所有的元素范围是[-1000, 1000]。
输入的数组中任意三个数的乘积不会超出32位有符号整数的范围。

'''
class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        res = [nums[-3]*nums[-2]*nums[-1], nums[0]*nums[1]*nums[-1]]
        return max(res)
    #主要考虑到若为正整数列表，则取最大的三个数，若列表中有正有负，则还需取最大的一个数，和最小的两个数
