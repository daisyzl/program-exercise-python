#-*-coding:utf-8-*-
'''
在排序数组中查找元素的第一个和最后一个位置

题目：https://leetcode-cn.com/explore/learn/card/binary-search/211/template-iii/844/

答案：https://blog.csdn.net/qqxx6661/article/details/81742268

给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

你的算法时间复杂度必须是 O(log n) 级别。

如果数组中不存在目标值，返回 [-1, -1]。

示例 1:

输入: nums = [5,7,7,8,8,10], target = 8
输出: [3,4]
示例 2:

输入: nums = [5,7,7,8,8,10], target = 6
输出: [-1,-1]


'''

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums)==0:
            return [-1,-1]
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target:
                l=r=mid
                #这个等式是最关键的
                while l-1>=0 and nums[l-1]==target:
                    l-=1
                while r+1<len(nums) and nums[r+1] == target:
                    r+=1
                return [l,r]
            #以上我们继续分头向前向后循环，直到找到不等于target的值，此时就能找到我们需要的索引对
            elif nums[mid]<target:
                l = mid+1
            else:
                r = mid-1
        return [-1,-1]