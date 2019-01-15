#-*-coding:utf-8-*-
'''

nums = [2, 3, 1, 5, 1, 2]
result = [3, 5]
提取没有重复数组
'''
class Solution():
    def test(self, nums):
        n  = len(nums)
        for i in nums:
            p = nums.count(i)
            if p > 1 :
                for j in range(p):
                    nums.remove(i)

        return nums


if __name__ == '__main__':
    nums = [2, 3, 1, 5, 1, 2]
    print(Solution().test(nums))



