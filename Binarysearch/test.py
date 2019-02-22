#-*-coding:utf-8-*-

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 1, n
        while l <= r:
            mid = (l+r)//2
            if guess(mid) == 0:
                return mid
            elif guess(mid) == -1:
                l = mid+1
            else:
                r = mid-1
        return -1