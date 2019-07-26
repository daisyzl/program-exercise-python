#-*-coding:utf-8-*-

'''
杨辉三角

题目：https://leetcode-cn.com/explore/learn/card/array-and-string/199/introduction-to-2d-array/776/

杨辉三角
给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。



在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:

输入: 5
输出:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

'''


class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []
        for i in range(numRows):
            temp = [0] * (i + 1)
            #先对一行数据进行定义，因为要对最后一个数赋值1
            temp[0], temp[-1] = 1, 1
            for j in range(1, i):
                temp[j] = result[i-1][j-1] + result[i-1][j]
                #注意取result的值
            result.append(temp)
        #注意把一位数组跑完了，再装入result里面
        #注意这是对二维数组的操作
        return result


    def generate1(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []
        for i in range(numRows):
            temp = [0] * (i + 1)
            temp[0],temp[-1] = 1,1
            for j in range(1, i):
                temp[j] = result[i - 1][j - 1] + result[i - 1][j]
            result.append(temp)
        return result

if __name__ == '__main__':
    print(Solution().generate(10))