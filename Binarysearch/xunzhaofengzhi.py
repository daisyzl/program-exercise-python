#-*-coding:utf-8-*-

'''
寻找峰值

题目：https://leetcode-cn.com/problems/find-peak-element/

复杂度：O(logN)   用二分法

答案：https://blog.csdn.net/qq_17550379/article/details/83780912

思想：由于两端都是负无穷，因此只要左右两端任一端比中点大，意味着那一侧有峰

峰值元素是指其值大于左右相邻值的元素。

给定一个输入数组 nums，其中 nums[i] ≠ nums[i+1]，找到峰值元素并返回其索引。

数组可能包含多个峰值，在这种情况下，返回任何一个峰值所在位置即可。

你可以假设 nums[-1] = nums[n] = -∞。

示例 1:

输入: nums = [1,2,3,1]
输出: 2
解释: 3 是峰值元素，你的函数应该返回其索引 2。
示例 2:

输入: nums = [1,2,1,3,5,6,4]
输出: 1 或 5
解释: 你的函数可以返回索引 1，其峰值元素为 2；
     或者返回索引 5， 其峰值元素为 6。
     只能返回一个
说明:

你的解法应该是 O(logN) 时间复杂度的。

'''

class Solution():
    def findPeakElement(self, nums):
        left = 0
        right = len(nums)-1
        while left <= right:
            print (left, right)
            if left == right:
                return left
            mid = (left+right) // 2
            # 如果中间小于右边，那么一定在右边
            if nums[mid] < nums[mid+1]:
                left = mid + 1
            # 左边不小于右边，那么直接把右边弄到中间
            else:
                # right不可以是mid-1，万一正好是mid，就跳过了，因为并没有比对mid的值
                right = mid

if __name__ == "__main__":
    nums = [1,2,1,3,5,6,4]
    nums1 =[1,2,3,1]
    print(Solution().findPeakElement(nums1))
