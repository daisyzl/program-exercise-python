#-*-coding:utf-8-*-

class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = 0
        result = []
        for i in nums:
            if i == 1:
                cnt += 1
                print(cnt)

            else:
                if cnt != 0:
                    result.append(cnt)
                cnt = 0
        print(result)
        if result is not None:

            return result.sort()[-1]
        else:
            return cnt

if __name__ == '__main__':

    print(Solution().findMaxConsecutiveOnes([1]))