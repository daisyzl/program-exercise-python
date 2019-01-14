#-*-coding:utf-8-*-

class Solution(object):
    def _binarySearch(self, arr, s):
        l, r = 0, len(arr)-1
        while l<=r:
            mid = (l+r)//2
            if arr[mid] == s:
                return mid
            elif arr[mid] < s:
                l = mid+1
            else:
                r = mid-1
        return -1

    def twoSum(self, nums, t):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """


        for i in range(len(nums)):
            temp = self._binarySearch(nums[i+1:], t-nums[i])
            if temp != -1:
                return [i+1, temp+2+i]
        return -1



if __name__ == '__main__':
    nums=[2, 7, 11, 15]
    t=9
    result =Solution().twoSum(nums,t)
    print(result)
