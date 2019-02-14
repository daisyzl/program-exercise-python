#-*-coding:utf-8-*-
'''
数组拆分 I

思想：要先排序，这样小的元素和除了它外最小的组合才不会牺牲大的。这样和才会最大。
这里用了python list中的sort方法来进行排序。

题目：https://leetcode-cn.com/explore/learn/card/array-and-string/201/two-pointer-technique/784/

给定长度为 2n 的数组, 你的任务是将这些数分成 n 对, 例如 (a1, b1), (a2, b2), ..., (an, bn) ，使得从1 到 n 的 min(ai, bi) 总和最大。

示例 1:

输入: [1,4,3,2]

输出: 4
解释: n 等于 2, 最大总和为 4 = min(1, 2) + min(3, 4).
提示:

n 是正整数,范围在 [1, 10000].
数组中的元素范围在 [-10000, 10000].

'''

class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        listNum = list(nums)
        listNum.sort()
        sum1 = 0
        #这个sum变量不能随便用，容易与sum函数起冲突
        #当这两个名称重复时，程序会默认调用Int型对象，但Int对象没有什么调用可言，就爆出了这个错误，解决方法也很简单，要么更改变量名，要么更改方法名。TypeError: 'int' object is not callable
        result = listNum[::2]
        print(sum(result))
        for i in range(0, len(listNum), 2):
            sum1 += listNum[i]
        return sum
if __name__ == '__main__':
    nums = [1,4,3,2]
    print(sum(nums[::2]))
    print(Solution().arrayPairSum(nums))