#-*-coding:utf-8-*-
'''

合并两个有序数组

题目：https://leetcode-cn.com/problems/merge-sorted-array/submissions/

结果：https://blog.csdn.net/qq_17550379/article/details/80500807

给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。

说明:

初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
示例:

输入:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

输出: [1,2,2,3,5,6]


'''

class Solution(object):
    #第一种方法无法运行
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        end = nums1[n-1]
        for i in range(n + m):
            if nums1[i] > nums2[0]:
                nums1.insert(i, nums2.pop(0))
                print(nums1)
                print(nums2)
            print("aaaaa")
            print(nums1)
            if nums1[i] == end :
                nums1[i+1:] = nums2[1:]

    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        #从后往前计算
        pos = m + n -1
        n -= 1
        m -= 1
        while n >= 0 and m >= 0:
            if nums1[m] > nums2[n]:
                nums1[pos] = nums1[m]
                m -= 1
                pos -= 1
            else:
                nums1[pos] = nums2[n]
                pos -= 1
                n -= 1
        while n >= 0:
            nums1[pos] = nums2[n]
            pos -= 1
            n -= 1

    def merge2(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        l = m + n
        while m > 0 and n > 0:
            if nums1[m - 1] < nums2[n - 1]:
                print(l-1)
                print(nums2[n - 1])
                nums1[l-1] = nums2[n - 1]
                print(nums1[l - 1])
                n -= 1
            else:
                nums1[l - 1] = nums1[m - 1]
                print(nums1[l - 1])
                m -= 1
            l -= 1
        print("aaaa")
        print(nums1)
        print(m)
        print(n)
        # nums1[:l + 1] += nums1[:m-1]
        # print(nums1[:l + 1] )
        # nums1[:l + 1] += nums2[:n]
        # print(nums1[:l + 1])
        # print(nums1)

        #注意下面只用算nums2，因为nums1本来就在结果集里
        while n>0:
            nums1[l-1] = nums2[n-1]
            n -= 1
            l -= 1
        print(nums1)



if __name__ == '__main__':
    nums1 = [1,2,3,0,0,0]
    nums2 = [2,5,6]
    m = 3
    n = 3
    #注意下面的测试用例中，nums11是空的
    nums11 = [0]
    nums22 = [1]
    m1 = 0
    n2 = 1

    print(Solution().merge2(nums11, m1,nums22,n2))