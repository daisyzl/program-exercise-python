#-*-coding:utf-8-*-
'''
螺旋矩阵2
题目：https://leetcode-cn.com/problems/spiral-matrix-ii/

答案：https://github.com/luliyucoordinate/Leetcode/blob/master/src/0054-Spiral-Matrix/0054.py

思想：https://blog.csdn.net/qq_17550379/article/details/83186516

给定一个正整数 n，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。

示例:

输入: 3
输出:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]


'''

class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[0] * n for i in range(n)]
        #注意这句话在创建二维数组
        m, n = len(matrix), len(matrix[0])
        x1, y1, x2, y2, k = 0, 0, m-1, n-1, 1
        #注意m-1, n-1 下面方便好计算
        while x1 <= x2 and y1 <= y2:
            for i in range(x1,x2 + 1):
                matrix[y1][i] = k
                k +=1
            for j in range(y1+1,y2+1):
                matrix[j][x2] = k
                k += 1
            if x1 < x2 and y1< y2:
                for i in range(x2-1, x1, -1):
                    matrix[y2][i] = k
                    k += 1
                for j in range(y2, y1, -1):
                    matrix[j][x1] = k
                    k += 1
            x1 +=1
            y1 +=1
            x2 -=1
            y2 -=1
        return matrix
if __name__ == '__main__':
    print(Solution().generateMatrix(3))




