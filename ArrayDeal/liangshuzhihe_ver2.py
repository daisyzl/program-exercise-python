#-*-coding:utf-8-*-

'''
题目：
https://leetcode-cn.com/explore/orignial/card/all-about-array/232/two-pointers/963/

解题思路：二分查找

这个时候算法的复杂度变成了O(nlogn)

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
    def _BinarySearch(self, nums, target):
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid+1
            else:
                right = mid
        if left != len(nums) and nums[left] == target:
            return left
        return -1
    def twoSum(self, nums, target):
        n = len(nums)
        for i in range(n):
            temp = self._BinarySearch(nums[i+1:], target-nums[i])
            if temp != -1:
                return [i+1, temp+i+2]
            #注意返回的temp+i+2容易忽视，返回的下标值（index1 和 index2）不是从零开始的
        return -1

if __name__ == '__main__':
    numbers = [2, 7, 11, 15]
    target = 9
    result = Solution().twoSum(numbers, target)
    print(result)
