#-*-coding:utf-8-*-
'''

至少是其他数字两倍的最大数
自己写的
主要是学习python的列表乘法语法，可以不用写，暴力方法

题目：https://leetcode-cn.com/problems/largest-number-at-least-twice-of-others/

在一个给定的数组nums中，总是存在一个最大元素 。

查找数组中的最大元素是否至少是数组中每个其他数字的两倍。

如果是，则返回最大元素的索引，否则返回-1。

示例 1:

输入: nums = [3, 6, 1, 0]
输出: 1
解释: 6是最大的整数, 对于数组中的其他整数,
6大于数组中其他元素的两倍。6的索引是1, 所以我们返回1.


示例 2:

输入: nums = [1, 2, 3, 4]
输出: -1
解释: 4没有超过3的两倍大, 所以我们返回 -1.


提示:

nums 的长度范围在[1, 50].
每个 nums[i] 的整数范围在 [0, 99].

'''
class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<=1:
            return 0
        #注意这种特殊情况输入为[1]
        m = max(nums)
        temp = nums.copy()
        #注意这里用copy，不要用nums = temp
        temp.remove(m)
        n = max(temp)
        if m >= n*2:
            return nums.index(m)
        return -1

    def dominantIndex2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = max(nums) * 2
        print(a)
        print(nums * 2)
        #注意将字符串和列表与数x相乘时，将重复这个序列x次来创建一个新序列
        print(max(nums * 2 ))

        if a == max([ x*2 for x in nums]):
            #这个方法很好，利用列表对list与数进行乘法运算
            return nums.index(max(nums))
        else:
            return -1




if __name__ == "__main__":
    nums=[0,0,2,3]
    nums1 = [0,0,0,1]
    print(Solution().dominantIndex3(nums))