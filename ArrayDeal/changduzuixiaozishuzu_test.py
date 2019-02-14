#-*-coding:utf-8-*-

class Solution():
    def minSubArrayLen(self, nums, s):
        n = len(nums)
        index_temp = n+1
        for i in range(n):
            temp = 0
            for j, val in enumerate(nums[i:]):
                temp += val
                if temp >= s:
                    index_temp = min(index_temp, j+1)
        if index_temp == n+1:
            return 0
        return index_temp

