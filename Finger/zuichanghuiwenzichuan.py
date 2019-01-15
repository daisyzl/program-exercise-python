#-*-coding:utf-8-*-

'''
题目：最长回文子串
https://leetcode-cn.com/problems/longest-palindromic-substring/

推荐方法为动态规划

没有实现


'''

class Solution:

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        l, r =0, 0
        n = len(s)
        max_length= 0
        temp = ""
        while l<=r and l<len(s) and r<len(s):
            arr = s[l:r+1]
            #回文操作需要复制给一个变量，再进行回文的，倒叙输出很复杂
            if arr[:] == arr[::-1]:
                print("arr[:]",arr[:])
                print("arr[::-1]",arr[::-1])
                print("max_length",max_length)
                print("L,R",l,r)
                if max_length!=max(max_length, r-l+1):
                    temp = s[l:r+1]
                    print("temp",temp)

                r+=1
                l+=1
            else:
                r+=1
            print("L2,R2", l, r)
        return temp

if __name__ == '__main__':
    print(Solution().longestPalindrome('babad'))
