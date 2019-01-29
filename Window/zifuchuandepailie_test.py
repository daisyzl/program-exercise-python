#-*-coding:utf-8-*-

class Solution():
    def checkInclusion(self, s1, s2):
        cnt1 = [0] * 26
        cnt2 = [0] * 26
        for i in s1:
            cnt1[ord(i) - ord('a')] += 1
        for j in range(len(s2)):
            cnt2[ord(s2[j]) - ord('a')] += 1
            if j < len(s1) -1:
                continue
            if cnt2 == cnt1:
                return True
            cnt2[ord(s2[j - len(s1) + 1]) - ord('a')] -= 1
        return False

if __name__ == '__main__':
    s1="ab"
    s2="eidbaooo"
    print(Solution().checkInclusion(s1,s2))
