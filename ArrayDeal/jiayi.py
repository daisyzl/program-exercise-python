#-*-coding:utf-8-*-
'''
加一

这道题值得借鉴，多写写

题目：https://leetcode-cn.com/explore/learn/card/array-and-string/198/introduction-to-array/772/

答案：https://blog.csdn.net/qq_34364995/article/details/80284300

给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储一个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

示例 1:

输入: [1,2,3]
输出: [1,2,4]
解释: 输入数组表示数字 123。
示例 2:

输入: [4,3,2,1]
输出: [4,3,2,2]
解释: 输入数组表示数字 4321。

备注：两个方法一样，第二种少一层判断

'''

class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if len(digits) == 0:
            digits = [1]
        elif digits[-1] == 9:
            digits = self.plusOne(digits[:-1])
            #倒数前一位数之前
            digits.append(0)
        else:
            digits[-1] +=1
            #注意取倒数第一个数
        return digits

    def plusOne2(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)
        if digits[-1] != 9:
            digits[-1] += 1
        else:
            digits = self.plusOne(digits[:-1])
            digits.append(0)
        return digits

if __name__ == '__main__':
    digits = [9]
    digits2 = [4, 3, 9]
    print(digits[-1: -3])
    #这样输出的结果为空
    print(digits[-3:-1])
    #[3, 2]
    print(Solution().plusOne2(digits))