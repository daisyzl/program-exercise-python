#-*-coding:utf-8-*-
'''
验证回文串

题目：https://leetcode-cn.com/problems/valid-palindrome/

答案：https://blog.csdn.net/qq_17550379/article/details/80514285

给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

说明：本题中，我们将空字符串定义为有效的回文串。

示例 1:

输入: "A man, a plan, a canal: Panama"
输出: true
示例 2:

输入: "race a car"
输出: false

'''

class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #不知道为什么leetcode无法通过
        s_filter = ''.join(filter(str.isalnum, s)).lower()
        #主要学习filter
        # isalnum() 方法检测字符串是否由字母和数字组成
        return s_filter[::-1] == s_filter

if __name__ == '__main__':
    s = "A man, a plan, a canal: Panama"
    s1 = "race a car"
    print(Solution().isPalindrome(s1))


