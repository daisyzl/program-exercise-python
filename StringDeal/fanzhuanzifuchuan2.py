#-*-coding:utf-8-*-
'''
反转字符串 II

这道题可以好好复习一下切片和一部分迭代

题目：https://leetcode-cn.com/problems/reverse-string-ii/

答案：https://blog.csdn.net/weixin_40449300/article/details/81048871


给定一个字符串和一个整数 k，你需要对从字符串开头算起的每个 2k 个字符的前k个字符进行反转。如果剩余少于 k 个字符，
则将剩余的所有全部反转。如果有小于 2k 但大于或等于 k 个字符，则反转前 k 个字符，并将剩余的字符保持原样。

示例:

输入: s = "abcdefg", k = 2
输出: "bacdfeg"
要求:

该字符串只包含小写的英文字母。
给定字符串的长度和 k 在[1, 10000]范围内


'''


class Solution:
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if len(s) <= k:
            return s[::-1]
        elif len(s) > k and len(s) <= 2*k:
            print(s[:k:-1])
            #步长为负数时，第一个索引必须比第二个索引大
            s = s[:k][::-1] + s[k: ][::-1]
        else:
            s = s[:k][::-1] + s[k: 2*k][::-1] + self.reverseStr(s[2*k:], k)
        return s

if __name__ == '__main__':
    s = "abcdefg"
    k = 2
    print(Solution().reverseStr(s,k))