#-*-coding:utf-8-*-
'''
单词模式

整道题拿笔画下好理解

题目：https://leetcode-cn.com/problems/word-pattern/

答案：https://blog.csdn.net/qq_17550379/article/details/80586058

给定一种 pattern(模式) 和一个字符串 str ，判断 str 是否遵循相同的模式。

这里的遵循指完全匹配，例如， pattern 里的每个字母和字符串 str 中的每个非空单词之间存在着双向连接的对应模式。

示例1:

输入: pattern = "abba", str = "dog cat cat dog"
输出: true
示例 2:

输入:pattern = "abba", str = "dog cat cat fish"
输出: false
示例 3:

输入: pattern = "aaaa", str = "dog cat cat dog"
输出: false
示例 4:

输入: pattern = "abba", str = "dog dog dog dog"
输出: false
说明:
你可以假设 pattern 只包含小写字母， str 包含了由单个空格分隔的小写字母。

'''

class Solution:
    #方法一的思想很好，用到了字典
    def wordPattern(self, pattern, str_):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        str_map1, str_map2 = {}, {}
        str_list = str_.split(' ')
        print(type(str_map1))

        str_list_len = len(str_list)
        p_list_len = len(pattern)
        if str_list_len != p_list_len:
            return False

        for i in range(p_list_len):
            if str_map1.get(pattern[i]) != str_map2.get(str_list[i]):
                return False
            print("aaaaa")
            print(pattern[i])
            print(str_map1.get(pattern[i]))
            str_map1[pattern[i]] = str_map2[str_list[i]] = i
        return True


    #方法二的思想很好
    def wordPattern2(self, pattern, str_):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        str_list = str_.split()
        print(str_list)
        n, m = len(pattern), len(str_list)
        print("n,m",n,m)
        if n != m:
            print("ddddddd")
            return False
        return len(set(zip(pattern, str_list)))==len(set(pattern))==len(set(str_list))
    #注意用到了三个连等号



if __name__ == '__main__':
    pattern = "abba"
    str = "dog cat cat dog"
    str2 = "dog cat cat fish"

    print(Solution().wordPattern2(pattern, str))