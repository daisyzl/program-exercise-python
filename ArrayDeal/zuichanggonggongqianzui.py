#-*-coding:utf-8-*-
'''
输入: ["flower","flow","flight"]
输出: "fl"
示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明:

所有输入只包含小写字母 a-z 。


https://leetcode-cn.com/explore/interview/card/bytedance/242/string/1014/

'''
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
        #str="",打印这一行数据
            return ""
        if len(strs) == 1:
            return strs[0]
        minl = min([len(x) for x in strs])
        end = 0
        while end < minl:
            for i in range(1,len(strs)):
                if strs[i][end]!= strs[i-1][end]:
                    #注意这是对列表→字符串的操作
                    return strs[0][:end]
                #注意这个return语句和下面的return语句的区别
            end += 1
            print(strs[0][:end])
        return strs[0][:end]

if __name__ == '__main__':
    str=["flower","flow","flight"]
    print(Solution().longestCommonPrefix(str))
