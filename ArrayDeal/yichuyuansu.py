#-*-coding:utf-8-*-

class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        list(set(nums)).remove(val)
        print(list(set(nums)).remove(val))
        return list(set(nums))

if __name__ == '__main__':
    nums = [1, 7, 3, 6, 5, 6]
    val = 6
    print(Solution().removeElement(nums, val))