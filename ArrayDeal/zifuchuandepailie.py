#-*-coding:utf-8-*-
'''

字符串的排列

给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的排列。
换句话说，第一个字符串的排列之一是第二个字符串的子串。

示例1:

输入: s1 = "ab" s2 = "eidbaooo"
输出: True
解释: s2 包含 s1 的排列之一 ("ba").

示例2:

输入: s1= "ab" s2 = "eidboaoo"
输出: False

注意：

输入的字符串只包含小写字母
两个字符串的长度都在 [1, 10,000] 之间

https://leetcode-cn.com/explore/interview/card/bytedance/242/string/1016/

http://www.cnblogs.com/MrSaver/p/9638279.html

'''


class Solution:
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        cnt1 = [0] * 26;
        cnt2 = [0] * 26;
        for c in s1:
            cnt1[ord(c) - ord('a')] += 1
        for i in range(len(s2)):
            cnt2[ord(s2[i]) - ord('a')] += 1
            if i < len(s1) - 1:
                continue
            #窗口的大小要和s1一致
            if cnt2 == cnt1:
                return True
            cnt2[ord(s2[i - len(s1) + 1]) - ord('a')] -= 1
            #为了使窗口进行移动
        return False

if __name__ == '__main__':
    s1="ab"
    s2="eidbaooo"
    print(Solution().checkInclusion(s1,s2))
