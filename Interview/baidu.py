#-*-coding:utf-8-*-

'''
nums = [1, 3, 2, 3, 5, 5, 5]
输出：[1, 3, 2, 3, 5]

去掉连续重复的数组

'''

class Solution():
    def test(self, nums):
        n = len(nums)
        result = []
        result.append(nums[0])
        for i in range(1,n):
            if nums[i] != nums[i-1]:
                result.append(nums[i])
        return result

if __name__ == '__main__':
    nums = [1, 3, 2, 3, 5, 5, 5]

    print(Solution().test(nums))



