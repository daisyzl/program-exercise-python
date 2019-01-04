#-*-coding:utf-8-*-
def lengthOfLongestSubstring(s):
    max_len=0
    if s is None or len(s)<1:
        return max_len
    str_dict={}
    start=0
    one_max=0
    for i in range(len(s)):
        if s[i] in str_dict and str_dict[s[i]]>start:
            start=str_dict[s[i]]+1
        one_max=i-start+1
        str_dict[s[i]]=i







if __name__ == '__main__':
    nums=[1,5,8,4,7,6,5,3,1]


    test=Solution().nextPermutation(nums)
    print(test)
