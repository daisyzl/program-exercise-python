#-*-coding:utf-8-*-
'''
寻找重复数
题目：https://leetcode-cn.com/explore/learn/card/binary-search/215/more-practices-ii/858/

答案：https://blog.csdn.net/qq_17550379/article/details/83893104

给定一个包含 n + 1 个整数的数组 nums，其数字都在 1 到 n 之间（包括 1 和 n），
可知至少存在一个重复的整数。假设只有一个重复的整数，找出这个重复的数。

示例 1:

输入: [1,3,4,2,2]
输出: 2
示例 2:

输入: [3,1,3,4,2]
输出: 3
说明：

不能更改原数组（假设数组是只读的）。
只能使用额外的 O(1) 的空间。
时间复杂度小于 O(n2) 。
数组中只有一个重复的数字，但它可能不止重复出现一次。

'''


class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low, high = 1, len(nums) - 1
        all = 0
        while low < high:
            mid = (high + low) // 2
            # for num in nums:
            #     all += num<=mid #叠加的是布尔值
            #     print("all",all)
            #与sum(num <= mid for num in nums)等价
            count = sum(num <= mid for num in nums)
            print("mid", mid)
            print("count",count)

            if count <= mid:
                low = mid + 1
            else:
                high = mid
        return low


if __name__ == "__main__":
    nums = [1, 3, 4, 2, 2, 2]
    print(Solution().findDuplicate(nums))