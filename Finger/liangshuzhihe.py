#-*-coding:utf-8-*-

'''
打卡：2019.1.14

题目：
https://leetcode-cn.com/explore/orignial/card/all-about-array/232/two-pointers/963/

解题思路：对撞指针法，又叫做双索引法，两个指针从左从右相遇

循环条件：while left < right:


差异：双向指针，这个指针都是从头开始，向左向右

O(n)的时间复杂度

解题答案：
https://blog.csdn.net/qq_17550379/article/details/80512745

两数之和 II - 输入有序数组
给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。

函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。

说明:

返回的下标值（index1 和 index2）不是从零开始的。
你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。
示例:

输入: numbers = [2, 7, 11, 15], target = 9
输出: [1,2]
解释: 2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。
'''

class Solution():
    def twoSum(self, nums, target):
        n = len(nums)
        left, right = 0, n-1
        while left < right:
            if nums[left] + nums[right] == target:
                return [left+1, right+1]
            elif nums[left] + nums[right] < target:
                left +=1
            else:
                right -=1
        return []

if __name__ == '__main__':
    numbers = [2, 7, 11, 15]
    target = 9
    result = Solution().twoSum(numbers, target)
    print(result)