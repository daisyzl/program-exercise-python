#-*-coding:utf-8-*-
''''
打卡时间：2019.1.15

给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

题目：
https://leetcode-cn.com/explore/interview/card/bytedance/242/string/1012/


'''
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        l, r = 0, 0
        max_length = 0
        s_list = list(s)
        #注意一定要把字符串整成数组才能执行下面的程序
        temp = []
        while l <= r and l < len(s) and r< len(s):
            #注意这个执行循环的条件
            if temp.count(s_list[r]) == 0:
                print(s_list[r])
                temp.append(s_list[r])
                print(temp)
                r += 1
                print("aaaa")
                print("L,R",l,r)
            else:
                temp.remove(s_list[r])
                print("cccc")
                print("L,R", l, r)
                l += 1
                print("bbbb")
                print("L,R",l,r)

            max_length = max(max_length, r - l)
            #注意这里就是r-l，不用r-l+1,因为在退出循环前已经
        if l == len(s):
            return 1
        return max_length

if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring('abcabcbbd'))