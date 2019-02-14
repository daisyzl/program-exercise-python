#-*-coding:utf-8-*-

'''

打卡时间：2019.2.13

'''

class Solution():
    def minSubArrayLen(self, nums, s):
        l, r = 0, 0
        sum_all = 0
        n = len(nums)
        min_length = n+1
        while l <= r and r < n:
            if  sum_all < s:
                sum_all += nums[r]
                r += 1
            else:
                sum_all -= nums[l]
                l += 1
            if sum_all >= s:
                min_length = min(min_length, r-l)
        if min_length == n+1:
            return 0
        return min_length
if __name__ == '__main__':
    nums = [2,3,1,2,4,3]
    s = 7
    print(Solution().minSubArrayLen(nums, s))