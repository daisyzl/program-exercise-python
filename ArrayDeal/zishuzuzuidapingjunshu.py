#-*-coding:utf-8-*-
class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        if len(nums)<=1:
            return nums[0]
        if len(nums)==k:
            return sum(nums)/2
        temp =[]
        for i in range(k,len(nums)):
            temp.append(sum(nums[i-k:i]))
        return max(temp)/k
if __name__ == '__main__':
    nums = [1,12,-5,-6,50,3]
    k = 4
    print(Solution().findMaxAverage(nums, k))