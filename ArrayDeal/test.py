#-*-coding:utf-8-*-

class Solution():
    def minSubArrayLen(self, nums, s):
        l, r = 0, 0
        min_temp = len(nums)+1
        while l<=r and r<len(nums):
            if sum(nums[l:r+1]) >= s :
                min_temp = min(min_temp, r-l+1)
                l +=1
            else:
                r +=1
        if min_temp == len(nums)+1:
            return 0

        return min_temp



if __name__ == '__main__':
    nums = [2,3,1,2,4,3]
    s = 7
    result =Solution().minSubArrayLen(nums, s)
    print(result)
