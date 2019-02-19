#-*-coding:utf-8-*-
'''
杨辉三角II

题目：https://leetcode-cn.com/problems/pascals-triangle-ii/

给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。

在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:

输入: 3
输出: [1,3,3,1]
进阶：

你可以优化你的算法到 O(k) 空间复杂度吗？

'''
class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        p = [1]
        #别忘了在这里进行初始化
        if not rowIndex:
            return rowIndex
        for j in range(1,rowIndex):
            p = [1] + [p[i] + p[i+1] for i in range(len(p) - 1)] + [1]
        return p


    def getRow1(self, rowIndex):
        p = [1]
        for i in range(rowIndex):
            p = list(map(lambda x,y : x+y, p +[0] ,[0]+p))
            #map()函数接收两个参数，一个是函数，一个是Iterable，
            # map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
            #一般map的使用最后再用list生成列表
            print("p +[0]",p + [0])
            print("[0]+p", [0] + p)
            #后面加一个数0，前面加一个数0
        return p

if __name__ == '__main__':
    print(Solution().getRow(3))