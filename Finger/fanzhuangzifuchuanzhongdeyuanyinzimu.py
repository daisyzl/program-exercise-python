#-*-coding:utf-8-*-
'''
题目：https://leetcode-cn.com/problems/reverse-string/

答案：https://blog.csdn.net/qq_17550379/article/details/80515302

编写一个函数，以字符串作为输入，反转该字符串中的元音字母。

示例 1:

输入: "hello"
输出: "holle"
示例 2:

输入: "leetcode"
输出: "leotcede"


'''


class Solution(object):
    #方法一无法运行，但是作为反面教材
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        l, r = 0, len(s) - 1
        s_list = list(s)
        #一定要把str转换为list，因为下面在交换数据时，字符串无法交换数据
        while l <= r and r < len(s):
            print(s[l])
            while s[l] not in vowels and l<=r:
                l += 1
                print("l",l)
            #一定不能用在while里嵌套一个while，可能超出范围，用if—contine有好处，把最外面的while进行判断

            while s[r] not in vowels and l<=r:
                r -= 1
            s_list[l], s_list[r] = s_list[r], s_list[l]
            print("sasas ",l,r)
            l += 1
            r -= 1
        return "".join(s_list)

    #方法二通用方法
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ['a', 'u', 'e', 'i', 'o', 'A', 'U', 'E', 'I', 'O']
        l = 0
        r = len(s) - 1
        s = list(s)
        while l <= r and r<=len(s):
            if s[l] not in vowels :
                l += 1
                continue

            if s[r] not in vowels:
                r -= 1
                continue

            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        return ''.join(s)

#方法三更适合python
    def reverseVowels3(self, s):
        vowels = ['a', 'u', 'e', 'i', 'o', 'A', 'U', 'E', 'I', 'O']
        p = [i for i in s if i in vowels]
        #符合条件的元音，最后从后往前弹出
        return "".join([ i if i not in vowels else p.pop() for i in s])




if __name__ == '__main__':
    s = "leetcode"
    print(Solution().reverseVowels3(s))