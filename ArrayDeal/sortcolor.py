#-*-coding:utf-8-*-
'''
颜色分类

题目：
https://leetcode-cn.com/explore/orignial/card/all-about-array/231/apply-basic-algorithm-thinking/957/

给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

注意:
不能使用代码库中的排序函数来解决这道题。

示例:

输入: [2,0,2,1,1,0]
输出: [0,0,1,1,2,2]
进阶：

一个直观的解决方案是使用计数排序的两趟扫描算法。
首先，迭代计算出0、1 和 2 元素的个数，然后按照0、1、2的排序，重写当前数组。
你能想出一个仅使用常数空间的一趟扫描算法吗？

解题思路：
https://www.jianshu.com/p/0701434250c4

'''


class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n=[0]*3
        for i in nums:
            n[i] += 1
        nums.clear()
        #注意这种情况下就不用再重新定义nums列表了
        for j in range(len(n)):
            nums.extend([j] * n[j])
        return nums

if __name__ == '__main__':
    nums = [2,0,2,1,1,0]
    result =Solution().sortColors(nums)
    print(result)
