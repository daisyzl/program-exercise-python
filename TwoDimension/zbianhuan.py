#-*-coding:utf-8-*-
'''
z字型变换

题目：https://leetcode-cn.com/problems/zigzag-conversion/

使用的是方法一

答案：https://blog.csdn.net/xinxin100011/article/details/81258144

将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：

L   C   I   R
E T O E S I I G
E   D   H   N
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。

请你实现这个将字符串进行指定行数变换的函数：

string convert(string s, int numRows);
示例 1:

输入: s = "LEETCODEISHIRING", numRows = 3
输出: "LCIRETOESIIGEDHN"
示例 2:

输入: s = "LEETCODEISHIRING", numRows = 4
输出: "LDREOEIIECIHNTSG"
解释:

L     D     R
E   O E   I I
E C   I H   N
T     S     G


'''


class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        n = 0
        dir = False
        #初始化dir 方向一定要是false
        result = [""] * min(numRows, len(s))
        #初始化定义一个字符串
        for c in s:
            result[n] += c
            if n == 0 or n == numRows - 1:
                dir = not dir
            #注意这里一定要是if
            if dir:
                n += 1
            else:
                n -= 1
        #字符串转换为数组
        return "".join(result)

if __name__ == '__main__':
    s = "PAYPALISHIRING"
    numRows = 3
    print(Solution().convert(s, numRows))
