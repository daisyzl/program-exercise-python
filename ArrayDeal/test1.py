#-*-coding:utf-8-*-

class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<=1:
            return 0
        #注意这种特殊情况
        m = max(nums)
        temp = nums.copy()
        #注意这里用copy，不要用nums = temp
        temp.remove(m)
        n = max(temp)
        if m >= n*2:
            return nums.index(m)
        return -1


if __name__ == "__main__":
    nums=[3, 6, 1, 0]
    nums1 = [0,0,0,1]
    print(Solution().dominantIndex(nums1))