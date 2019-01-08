#-*-coding:utf-8-*-
'''

字符串的排列

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
