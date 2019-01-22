#-*-coding:utf-8-*-
'''
两个数组的交集

题目：https://leetcode-cn.com/explore/learn/card/binary-search/214/more-practices/855/

答案：https://github.com/luliyucoordinate/Leetcode/blob/master/src/0349-Intersection-of-Two-Arrays/0349.py

给定两个数组，编写一个函数来计算它们的交集。

示例 1:

输入: nums1 = [1,2,2,1], nums2 = [2,2]
输出: [2]
示例 2:

输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出: [9,4]
说明:

输出结果中的每个元素一定是唯一的。
我们可以不考虑输出结果的顺序。

'''

class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = set([i for i in nums1 if i in nums2])
        print(result)
        '''
        >>> s = set([1, 2, 3])
        >>> s
        {1, 2, 3}
       '''
        return list(result)

    def intersection2(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return list(set(nums1) & set(nums2))

if __name__ == "__main__":
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    print(Solution().intersection(nums1, nums2))