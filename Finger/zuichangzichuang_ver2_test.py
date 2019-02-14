#-*-coding:utf-8-*-

class Solution:
    def lengthOfLongestSubstring(self, s):
        l, r = 0, 0
        max_length = 0
        s_list = list(s)
        temp = []
        while l <= r and l<len(s):
            if temp.count(s_list[r]) == 0:
                temp.append(s_list[r])
                r += 1
            else:
                temp.remove(s_list[l])
                l +=1
            max_length = max(max_length, r - l)
        return max_length



