#-*-coding:utf-8-*-
'''
按奇偶排序数组 II

题目：https://leetcode-cn.com/problems/sort-array-by-parity-ii/

答案：https://blog.csdn.net/qq_17550379/article/details/83048534

给定一个非负整数数组 A， A 中一半整数是奇数，一半整数是偶数。

对数组进行排序，以便当 A[i] 为奇数时，i 也是奇数；当 A[i] 为偶数时， i 也是偶数。

你可以返回任何满足上述条件的数组作为答案。


示例：

输入：[4,2,5,7]
输出：[4,5,2,7]
解释：[4,7,2,5]，[2,5,4,7]，[2,7,4,5] 也会被接受。


提示：

2 <= A.length <= 20000
A.length % 2 == 0
0 <= A[i] <= 1000
'''

class Solution(object):
    #方法一
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        result, odd, even = [], [], []
        for i in A:
            if i%2 == 0:
                #odd += i
            #整数不能这样叠加
                odd.append(i)
            else:
                even.append(i)
        # A中一半整数是奇数，一半整数是偶数。
        while odd and even:
            result.append(odd.pop(0))
            result.append(even.pop(0))
            #注意一个奇数一个偶数可以这样写
        return result

    # 方法二
    #只用开辟一个空间,两个指针也是从头开始

    def sortArrayByParityII2(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        n = len(A)
        i, j = 0, 1
        #i和j分别作为偶数和奇数的指针
        result = [0] * n
        for a in A:
            if a&1 == 0:
                #说明是偶数
                result[i] = a
                i+=2
            else:
                result[j] = a
                j+=2
        return result

    #方法三 不用耗费多余空间，两个指针都从头开始，方法不对，方法四是正确的
    def sortArrayByParityII3(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        i, j = 0, 1
        while i<len(A) and A[i] %2 == 0:
            i += 2
        while j<len(A) and A[j] %2 !=0:
            j += 2
        if i < len(A) and j < len(A):
            A[i], A[j] = A[j], A[i]
            i +=2
            j += 2
        return A

    def sortArrayByParityII4(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        i, j = 0, 1
        while i < len(A):
            if A[i] %2 != 0:
                while A[j]%2 != 0:
                    j+=2
                A[i],A[j] = A[j], A[i]
            i+=2
        return A



if __name__ == '__main__':
    A = [4,2,5,7]
    A1 =[2,3]
    print(Solution().sortArrayByParityII3(A1))

