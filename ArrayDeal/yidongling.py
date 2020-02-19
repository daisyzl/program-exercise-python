#-*-coding:utf-8-*-
'''


'''


class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = nums.count(0)

        for i in range(n):
            nums.remove(0)
        nums.extend([0]*n)
        print(nums)
if __name__ == '__main__':
    nums = [0,1,0,3,12]

    print(Solution().moveZeroes(nums))