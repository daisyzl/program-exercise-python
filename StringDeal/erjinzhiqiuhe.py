#-*-coding:utf-8-*-
'''
二进制求和

题目：https://leetcode-cn.com/explore/learn/card/array-and-string/200/introduction-to-string/779/

给定两个二进制字符串，返回他们的和（用二进制表示）。

输入为非空字符串且只包含数字 1 和 0。

示例 1:

输入: a = "11", b = "1"
输出: "100"
示例 2:

输入: a = "1010", b = "1011"
输出: "10101"

int的思想
https://www.cnblogs.com/wushuaishuai/p/7677992.html
'''

class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a_bin = int(a, 2)
        print(a_bin)
        #把字符串转换为10进制整数，认为a无论是字符串还是数字是二进制的形式
        b_bin = int(b, 2)
        print(b_bin)
        result = bin(a_bin + b_bin)
        print(result)
        #0b100
        return bin(int(a, 2) + int(b, 2))[2:]
        #要把0b去掉


    def addBinary2(self, a, b):
        n , m = int(a,2),int(b,10)
        print("qqqqqqq")
        print(n)
        return bin(n+m)[2:]

if __name__ == '__main__':
    a = '11'
    b = '1'

    print(Solution().addBinary(a, b))
