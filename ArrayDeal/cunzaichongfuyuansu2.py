#-*-coding:utf-8-*-
'''
存在重复元素 II

题目：https://leetcode-cn.com/problems/contains-duplicate-ii/submissions/

答案：https://blog.csdn.net/qq_17550379/article/details/80638690

给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，
使得 nums [i] = nums [j]，并且 i 和 j 的差的绝对值最大为 k。

示例 1:

输入: nums = [1,2,3,1], k = 3
输出: true
示例 2:

输入: nums = [1,0,1,1], k = 1
输出: true
示例 3:

输入: nums = [1,2,3,1,2,3], k = 2
输出: false

'''

class Solution(object):
    #暴力解法如果数组过长无法运行成功
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if not nums:
            return False
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j] and abs(j-i) <=k:
                    return True
        return False

    def containsNearbyDuplicate2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        record = set()
        for i, num in enumerate(nums):
            if num in record:
                return True

            record.add(num)
            print("aaaa")
            print(record)

            if len(record) == k + 1:
                record.remove(nums[i - k])
                print("ddddddd")
                print(record)

        return False



if __name__ == '__main__':
    nums = [1, 2, 3, 1, 2, 3]
    k = 2
    print(Solution().containsNearbyDuplicate2(nums, k))
