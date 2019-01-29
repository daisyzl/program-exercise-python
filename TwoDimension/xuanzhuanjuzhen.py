#-*-coding:utf-8-*-
'''
螺旋矩阵
题目：https://leetcode-cn.com/explore/learn/card/array-and-string/199/introduction-to-2d-array/775/

答案：https://github.com/luliyucoordinate/Leetcode/blob/master/src/0054-Spiral-Matrix/0054.py

思想：https://blog.csdn.net/qq_17550379/article/details/83148050

给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。

示例 1:

输入:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
输出: [1,2,3,6,9,8,7,4,5]
示例 2:

输入:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
输出: [1,2,3,4,8,12,11,10,9,5,6,7]


'''

class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return
        result = []
        #注意这里定义二维数组
        m, n = len(matrix), len(matrix[0])
        x1, y1, x2, y2 = 0, 0, m-1, n-1
        #注意m-1, n-1 下面方便好计算
        while x1 <= x2 and y1 <= y2:
            for i in range(x1,x2):
                result.append(matrix[y1][i])
            for j in range(y1+1,y2+1):
                result.append(matrix[j][x2])
            if x1 < x2 and y1< y2:
                for i in range(x2-1, x1, -1):
                    result.append(matrix[y2][i])
                for j in range(y2, y1, -1):
                    result.append(matrix[j][x1])
            x1 +=1
            y1 +=1
            x2 -=1
            y2 -=1
        return result


