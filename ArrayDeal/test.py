#-*-coding:utf-8-*-

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l, r = 0, 0
        max_length = 0
        s_list = list(s)
        temp = []
        while l <= r and l < len(s) and r< len(s):
            if temp.count(s_list[r]) == 0:
                print(s_list[r])
                temp.append(s_list[r])
                print(temp)
                r += 1
            else:
                temp.remove(s_list[r])
                l += 1

            max_length = max(max_length, r - l)
        if l == len(s):
            return 1
        return max_length

if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring('abcabcbb'))