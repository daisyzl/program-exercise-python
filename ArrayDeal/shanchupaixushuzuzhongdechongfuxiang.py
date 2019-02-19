#-*-coding:utf-8-*-

'''



'''
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        print(set(nums))
        return len(list(set(nums)))
if __name__ == '__main__':

    nums = [0,0,1,1,1,2,2,3,3,4]
    nums2 =[1,1,2]
    print(Solution().removeDuplicates(nums2))
