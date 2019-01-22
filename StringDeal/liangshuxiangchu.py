#-*-coding:utf-8-*-
'''
两数相除
题目：https://leetcode-cn.com/problems/divide-two-integers/
这道题挺难的，多看看

答案：https://blog.csdn.net/weixin_41958153/article/details/80797415

给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。

返回被除数 dividend 除以除数 divisor 得到的商。

示例 1:

输入: dividend = 10, divisor = 3
输出: 3
示例 2:

输入: dividend = 7, divisor = -3
输出: -2
说明:

被除数和除数均为 32 位有符号整数。
除数不为 0。
假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−231,  231 − 1]。本题中，如果除法结果溢出，则返回 231 − 1。

'''
class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        pos = False if (dividend < 0) ^ (divisor < 0) else True

        res, divd, divs = 0, abs(dividend), abs(divisor)

        if divd < divs:
            return 0

        mod = 2 ** 31
        while divs <= divd:
            mul, tmp = 1, divs
            while (tmp << 1) <= divd:
                mul <<= 1
                tmp <<= 1

            res += mul
            divd -= tmp

            if res == mod:
                break

        if pos and res == mod:
            res -= 1

        return res if pos else -res

if __name__ == '__main__':
    dividend = 7
    divisor = -3

    print(Solution().divide(dividend, divisor))