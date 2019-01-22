#-*-coding:utf-8-*-
'''
最长公告前缀

思想：可以多看下该思想

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
                if strs[i][end]!= strs[i-1][end]:#针对字符串每个字符进行操作，学习这种思想
                    #注意这是对列表→字符串的操作

                    print("sdsdsd")
                    return strs[0][:end]
                #注意这个return语句和下面的return语句的区别
            end += 1
        print(strs[0][:end])
        return strs[0][:end]

    def longestCommonPrefix1(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]
        n = len(strs)
        m = min([len(x) for x in strs])
        end = 0
        while end< m:
            for i in range(n - 1):
                if strs[i][end] != strs[i + 1][end]:
                    return strs[0][:end]
            end +=1
        return strs[0][:end]

'''
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]
        r = 0
        n = len(strs)
        m = min([len(x) for x in strs])
        for i in range(n - 1):
            r = 0
            for j in range(m):
                if strs[i][:r] != strs[i + 1][:r] :
                    #strs[i][:r] != strs[i + 1][:r] 如果r=0，strs[i][:r]=""，认为二者相等
                    print("dddddddd")
                    print("strs[i+1][:r]",strs[i+1][:r])
                    r -=1
                    return strs[0][:r]
                else:
                    r += 1
        return strs[0][:r]

'''
if __name__ == '__main__':
    str=["flower","flow","flight"]
    print(Solution().longestCommonPrefix1(str))
