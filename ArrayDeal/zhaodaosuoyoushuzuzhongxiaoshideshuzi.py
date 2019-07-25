#-*-coding:utf-8-*-
'''
找到所有数组中消失的数字

题目：https://leetcode-cn.com/problems/find-all-numbers-disappeared-in-an-array/

给定一个范围在  1 ≤ a[i] ≤ n ( n = 数组大小 ) 的 整型数组，数组中的元素一些出现了两次，另一些只出现一次。

找到所有在 [1, n] 范围之间没有出现在数组中的数字。

您能在不使用额外空间且时间复杂度为O(n)的情况下完成这个任务吗? 你可以假定返回的数组不算在额外空间内。

示例:

输入:
[4,3,2,7,8,2,3,1]

输出:
[5,6]
'''

class Solution(object):
    #这道题的弊端 较长数组无法通过
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        n = len(nums)
        for i in range(n):
            if (i + 1) not in nums:
                print(i+1)
                nums.append(i + 1)
        return nums[n:]

#
    def findDisappearedNumbers2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return list(set(range(1, len(nums)+1)) - set(nums))
    #两个set进行去重操作

    def findDisappearedNumbers3(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s = set(nums)  # 不能直接写成一行，效率太低
        return [i for i in range(1, len(nums) + 1) if i not in s]


if __name__ == '__main__':

    nums =[4,3,2,7,8,2,3,1]
    print(Solution().findDisappearedNumbers(nums))