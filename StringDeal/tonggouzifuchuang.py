#-*-coding:utf-8-*-
'''
题目：同构字符串

题目：https://leetcode-cn.com/problems/isomorphic-strings/submissions/

答案：https://blog.csdn.net/qq_17550379/article/details/80586172


所有出现的字符都必须用另一个字符替换，同时保留字符的顺序。两个字符不能映射到同一个字符上，但字符可以映射自己本身。

示例 1:

输入: s = "egg", t = "add"
输出: true
示例 2:

输入: s = "foo", t = "bar"
输出: false
示例 3:

输入: s = "paper", t = "title"
输出: true
说明:
你可以假设 s 和 t 具有相同的长度。

'''

class Solution(object):
    #方法一
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        s_dict, t_dict = {}, {}
        if len(s) != len(t):
            print("dsss")
            return False
        for i in range(len(s)):
            if s_dict.get(s[i]) != t_dict.get(t[i]):
                return False
            s_dict[s[i]] = t_dict[t[i]] = i
        return True

        #方法二
        def isIsomorphic(self, s, t):
            """
            :type s: str
            :type t: str
            :rtype: bool
            """
            if len(s) != len(t): return False
            return len(set(s)) == len(set(t)) == len(set(zip(s, t)))

if __name__ == '__main__':
    s = "foo"
    t = "bar"
    s2 = "egg"
    t2 = "add"

    print(Solution().isIsomorphic(s2,t2))