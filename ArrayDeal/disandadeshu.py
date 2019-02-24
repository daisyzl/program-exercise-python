#-*-coding:utf-8-*-
'''
第三大的数leetcode 第三大的数 python

题目：https://leetcode-cn.com/problems/third-maximum-number/submissions/

给定一个非空数组，返回此数组中第三大的数。如果不存在，则返回数组中最大的数。要求算法时间复杂度必须是O(n)。

示例 1:

输入: [3, 2, 1]

输出: 1

解释: 第三大的数是 1.
示例 2:

输入: [1, 2]

输出: 2

解释: 第三大的数不存在, 所以返回最大的数 2 .
示例 3:

输入: [2, 2, 3, 1]

输出: 1

解释: 注意，要求返回第三大的数，是指第三大且唯一出现的数。
存在两个值为2的数，它们都排第二。

'''
class Solution(object):

    #方法一 由自己完成有些繁琐
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        nums.sort(reverse = True)
        #注意这样写是将列表值进行倒序，nums.reverse()是将列表的index倒序，二者有区别
        print(nums)
        cnt = 1
        for i in range(len(nums) - 1):
            print("ssss")
            print(nums[i])
            if nums[i] > nums[i + 1]:
                cnt += 1
                print("aaaa")
                print(nums[i])

            if cnt == 3:
                print("bbbbb")
                print(nums[i+1])
                return nums[i + 1]
        return max(nums)

    def thirdMax2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = list(set(nums))
        temp.sort(reverse=True)
        if len(temp) <= 2:
            return temp[0]
        else:
            return temp[2]





if __name__ == '__main__':
    nums = [3, 2, 4, 1]
    nums1 = [1,2]
    print(Solution().thirdMax(nums))