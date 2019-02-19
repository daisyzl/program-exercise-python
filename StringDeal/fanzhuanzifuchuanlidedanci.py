#-*-coding:utf-8-*-
'''
翻转字符串里的单词

题目：https://leetcode-cn.com/explore/learn/card/array-and-string/202/conclusion/793/

给定一个字符串，逐个翻转字符串中的每个单词。

示例:

输入: "the sky is blue",
输出: "blue is sky the".
说明:

无空格字符构成一个单词。
输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。
进阶: 请选用C语言的用户尝试使用 O(1) 空间复杂度的原地解法。


'''

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = []
        print(len(s))
        #输出15
        return " ".join(s.split()[::-1])
    #注意这里一定要带空格

if __name__ == '__main__':
    strs = "the sky is blue"
    print(Solution().reverseWords(strs))
