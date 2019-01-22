#-*-coding:utf-8-*-

'''
x 的平方根

题目：https://leetcode-cn.com/explore/learn/card/binary-search/209/template-i/836/

答案：https://www.cnblogs.com/NPC-assange/p/9362756.html

实现 int sqrt(int x) 函数。

计算并返回 x 的平方根，其中 x 是非负整数。

由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

示例 1:

输入: 4
输出: 2
示例 2:

输入: 8
输出: 2
说明: 8 的平方根是 2.82842...,
     由于返回类型是整数，小数部分将被舍去。



'''

class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        l, r = 1, x
        while l <= r:
            mid = (l+r)//2
            v = mid * mid
            if v == x:
                return mid
            elif v<x:
                l = mid+1
            else:
                r = mid-1
        return r
    #注意最后不符合条件返回的是r