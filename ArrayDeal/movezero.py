#-*-coding:utf-8-*-

'''
移动零

注意append和extend的使用

给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

示例:

输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
说明:

必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数。

题目：
https://leetcode-cn.com/explore/orignial/card/all-about-array/230/define-with-good-care/948/


'''


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = nums.count(0)
        for i in range(n):
            nums.remove(0)
        nums.extend([0]*n)
        print(nums.append([0]*n))
        print("aaaaa")
        print([0]*n)
        [0, 0]
        #注意append和extend的区别
        return nums

'''
list的remove方法删除第一个为指定值的元素，没有的话会报错
'''

if __name__ == '__main__':
    nums =[0,1,0,3,12]
    result = Solution().moveZeroes(nums)
    print(result)
